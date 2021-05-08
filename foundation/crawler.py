import json
from urllib import parse, request

from foundation import get_api_key
from ptu_bus.models import BusTerminal, BusTimeTable
from ptu_train.models import TrainTerminal, TrainTimeTable


class BaseCrawler:
    def __init__(self):
        self.api_key = get_api_key()
        self.queryset.delete()

    def make_url(self, url: str):
        return url + parse.urlencode(self.query, encoding="UTF-8", doseq=True)

    def open_url(self, url: str):
        url = self.make_url(url)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return json.loads(response.read().decode("utf-8"))

    def collect_data(self):
        raise NotImplementedError


class BusTerminalCrawler(BaseCrawler):
    queryset = BusTerminal.objects.all()

    def __init__(self, cid="1220"):
        super().__init__()
        self.url = [
            {
                "url": "https://api.odsay.com/v1/api/intercityBusTerminals?",
                "is_express": 0,
            },
            {
                "url": "https://api.odsay.com/v1/api/expressBusTerminals?",
                "is_express": 1,
            },
        ]
        self.query = [("apiKey", self.api_key), ("CID", cid)]
        self.pyeong_taek_station_name = ["평택시외버스터미널", "평택고속버스터미널"]

    def collect_data(self):
        key = 1
        for bus_type in self.url:
            odsay_data = self.open_url(bus_type["url"])
            is_express = bus_type["is_express"]
            for start_terminal in odsay_data["result"]:
                if (
                    start_terminal["haveDestinationTerminals"]
                    and start_terminal["stationName"] in self.pyeong_taek_station_name
                ):
                    for destination_terminal in start_terminal["destinationTerminals"]:
                        BusTerminal(
                            key=key,
                            start_station_name=start_terminal["stationName"],
                            start_station_id=start_terminal["stationID"],
                            end_station_name=destination_terminal["stationName"][
                                destination_terminal["stationName"].find("/") + 1 :
                            ],
                            end_station_id=destination_terminal["stationID"],
                            is_express=int(is_express),
                        ).save()
                        key += 1


class BusTimeTableCrawler(BaseCrawler):
    queryset = BusTimeTable.objects.all()

    def __init__(self):
        super().__init__()
        self.bus_terminal_data = BusTerminal.objects.all()
        self.url = [
            "https://api.odsay.com/v1/api/intercityServiceTime?",
            "https://api.odsay.com/v1/api/expressServiceTime?",
        ]

    def split_schedule(self, schedule: str):
        replace_all = schedule.replace("/", " ")
        return "".join(replace_all).split()

    def min_2_hour(self, time: str):
        if time.find(":") == -1:
            time = int(time)
            hour = time // 60
            min = time % 60
            return str(hour).zfill(2) + ":" + str(min).zfill(2)
        else:
            return time

    def collect_data(self):
        key = 1
        for bus_terminal in self.bus_terminal_data:
            url = self.url[bus_terminal.is_express]

            self.query = [
                ("apiKey", self.api_key),
                ("startStationID", bus_terminal.start_station_id),
                ("endStationID", bus_terminal.end_station_id),
            ]

            odsay_data = self.open_url(url)

            bus_timetable_data = odsay_data["result"]["station"][0]
            schedules = self.split_schedule(bus_timetable_data.get("schedule"))

            if bus_timetable_data.get("specialFare"):
                special_fare = bus_timetable_data["specialFare"]
            else:
                special_fare = 0

            if bus_timetable_data.get("nightSchedule"):
                night_schedule = bus_timetable_data["nightSchedule"]
            else:
                night_schedule = "0"

            for schedule in schedules:
                BusTimeTable(
                    key=key,
                    bus_terminal=bus_terminal,
                    waste_time=self.min_2_hour(bus_timetable_data["wasteTime"]),
                    normal_fare=bus_timetable_data["normalFare"],
                    special_fare=special_fare,
                    night_fare=bus_timetable_data["nightFare"],
                    schedule=schedule,
                    night_schedule=night_schedule,
                ).save()
                key += 1


class TrainTerminalCrawler(BaseCrawler):
    queryset = TrainTerminal.objects.all()

    def __init__(self, cid="1220"):
        super().__init__()
        self.url = "https://api.odsay.com/v1/api/trainTerminals?"
        self.query = [("apiKey", self.api_key), ("CID", cid)]

    def collect_data(self):
        key = 1
        odsay_data = self.open_url(self.url)
        for start_terminal in odsay_data["result"]:
            if (
                start_terminal["haveDestinationTerminals"]
                and start_terminal["stationName"] in "평택"
            ):
                for arrival_terminal in start_terminal["arrivalTerminals"]:
                    TrainTerminal(
                        key=key,
                        start_terminal_id=start_terminal["stationID"],
                        start_terminal_name=start_terminal["stationName"],
                        end_terminal_id=arrival_terminal["stationID"],
                        end_terminal_name=arrival_terminal["stationName"],
                    ).save()
                    key += 1


class TrainTimeTableCrawler(BaseCrawler):
    queryset = TrainTimeTable.objects.all()

    def __init__(self):
        super().__init__()
        self.train_terminal_data = TrainTerminal.objects.all()
        self.url = "https://api.odsay.com/v1/api/trainServiceTime?"

    def collect_data(self):
        key = 1
        for train_terminal in self.train_terminal_data:
            self.query = [
                ("apiKey", self.api_key),
                ("startStationID", train_terminal.start_terminal_id),
                ("endStationID", train_terminal.end_terminal_id),
            ]

            odsay_data = self.open_url(self.url)

            train_timetable_data = odsay_data["result"]["station"]

            for result in train_timetable_data:
                TrainTimeTable(
                    key=key,
                    train_terminal=train_terminal,
                    rail_name=result["railName"],
                    train_class=result["trainClass"],
                    departure_time=result["departureTime"],
                    schedule=result["arrivalTime"],
                    waste_time=result["wasteTime"],
                    daily_type_code=result["runDay"],
                ).save()
                key += 1
