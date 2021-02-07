import json
from urllib import parse, request

from foundation import get_api_key
from ptu_bus.models import BusTerminal


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


if __name__ == "__main__":
    print(BusTerminalCrawler().collect_data())
