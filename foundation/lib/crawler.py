from urllib import parse, request

from foundation.lib import get_api_key


class BaseCrawler:
    def __init__(self):
        self.api_key = get_api_key()
        self.query = []

    def make_url(self, url):
        return url + parse.urlencode(self.query, encoding="UTF-8", doseq=True)

    def open_url(self, url):
        url = self.make_url(url)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode("utf-8")

    def parsing(self):
        raise NotImplementedError
