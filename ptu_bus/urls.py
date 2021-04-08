from django.urls import path

from ptu_bus.views import BusTerminalListView
from ptu_subway.views import (
    CrawlingSubwayLineData,
    CrawlingSubwayStationData,
)

urlpatterns = [
    path(
        "terminals/",
        BusTerminalListView.as_view(),
        name="bus_terminal_list_view ",
    ),
]
