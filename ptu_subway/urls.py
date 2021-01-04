from django.urls import path

from ptu_subway.views import (
    CrawlingSubwayLineData,
)

urlpatterns = [
    path(
        "crawling/lines/",
        CrawlingSubwayLineData.as_view(),
        name="crawling_subway_line_data",
    ),
]
