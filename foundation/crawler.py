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
        return response.read().decode("utf-8")

    def parsing(self):
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

    def parsing(self):
        for bus_type in self.url:
            data = self.open_url(bus_type["url"])
            is_express = bus_type["is_express"]
            t = data["result"]
            for i in range(len(t)):
                terminal_name = data["result"][i]["stationName"]
                if terminal_name == "평택시외버스터미널" or terminal_name == "평택고속버스터미널":
                    start_station_id = data["result"][i]["stationID"]
                    start_station_name = data["result"][i]["stationName"]
                    results = data["result"][i]["destinationTerminals"]
                    for result in results:
                        end_station_name = result["stationName"]
                        BusTerminal(
                            start_station_name=start_station_name,
                            start_station_id=start_station_id,
                            end_station_name=end_station_name[
                                end_station_name.find("/") + 1 :
                            ],
                            end_station_id=result["stationID"],
                            is_express=int(is_express),
                        ).save()


if __name__ == "__main__":
    import django

    django.setup()
    print(BusTerminalCrawler().parsing())
