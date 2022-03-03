from django.urls import path

from ptu_subway.views import (
    CrawlingSubwayLineData,
    CrawlingSubwayStationData,
)

urlpatterns = [
    path(
        "crawling/lines/",
        CrawlingSubwayLineData.as_view(),
        name="crawling_subway_line_data",
    ),
    path(
        "crawling/stations/",
        CrawlingSubwayStationData.as_view(),
        name="crawling_subway_station_data",
    ),
]
