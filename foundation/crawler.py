import json
from urllib import parse, request

import django

django.setup()

from foundation import get_api_key
from ptu_bus.models import BusTerminal, BusTimeTable


class BaseCrawler:
    def __init__(self):
        self.api_key = get_api_key()

    def make_url(self, url):
        return url + parse.urlencode(self.query, encoding="UTF-8", doseq=True)

    def open_url(self, url):
        url = self.make_url(url)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return json.loads(response.read().decode("utf-8"))

    def collect_data(self):
        raise NotImplementedError


class BusTerminalCrawler(BaseCrawler):
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
        for bus_type in self.url:
            odsay_data = self.open_url(bus_type["url"])
            is_express = bus_type["is_express"]
            for start_terminal in odsay_data["result"]:
                if (
                    start_terminal["haveDestinationTerminals"]
                    and start_terminal["stationName"] in self.pyeong_taek_station_name
                ):
                    for destination_terminal in start_terminal["destinationTerminals"]:
                        bus_terminal_filter = BusTerminal.objects.filter(
                            end_station_id=destination_terminal["stationID"]
                        )
                        if not bus_terminal_filter.exists():
                            BusTerminal(
                                start_station_name=start_terminal["stationName"],
                                start_station_id=start_terminal["stationID"],
                                end_station_name=destination_terminal["stationName"][
                                    destination_terminal["stationName"].find("/") + 1 :
                                ],
                                end_station_id=destination_terminal["stationID"],
                                is_express=int(is_express),
                            ).save()


class BusTimeTableCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.bus_terminal_data = BusTerminal.objects.all()
        self.url = [
            "https://api.odsay.com/v1/api/intercityServiceTime?",
            "https://api.odsay.com/v1/api/expressServiceTime?",
        ]

    def clean_schedule(self, schedule):
        replace_all = schedule.replace("/", " ")
        return "".join(replace_all).split()

    def min_2_hour(self, time):
        if time.find(":") == -1:
            time = int(time)
            hour = time // 60
            min = time % 60
            return str(hour).zfill(2) + ":" + str(min).zfill(2)
        else:
            return time

    def collect_data(self):
        for bus_terminal in self.bus_terminal_data:
            url = self.url[bus_terminal.is_express]

            self.query = [
                ("apiKey", self.api_key),
                ("startStationID", bus_terminal.start_station_id),
                ("endStationID", bus_terminal.end_station_id),
            ]

            odsay_data = self.open_url(url)

            bus_timetable_data = odsay_data["result"]["station"][0]
            schedules = self.clean_schedule(bus_timetable_data["schedule"])

            if bus_timetable_data.get("specialFare"):
                special_fare = bus_timetable_data["specialFare"]
            else:
                special_fare = 0

            if not bus_timetable_data["nightSchedule"]:
                night_schedule = bus_timetable_data["nightSchedule"]
            else:
                night_schedule = "0"

            for schedule in schedules:
                BusTimeTable(
                    bus_terminal=bus_terminal,
                    waste_time=self.min_2_hour(bus_timetable_data["wasteTime"]),
                    normal_fare=bus_timetable_data["normalFare"],
                    special_fare=special_fare,
                    night_fare=bus_timetable_data["nightFare"],
                    schedule=schedule,
                    night_schedule=night_schedule,
                ).save()


if __name__ == "__main__":
    BusTerminalCrawler().collect_data()
    print(BusTimeTableCrawler().collect_data())
