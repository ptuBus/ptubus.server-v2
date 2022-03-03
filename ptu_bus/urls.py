from django.urls import path

from .views import BusTerminalListView, BusTimeTableListView

urlpatterns = [
    path(
        "terminal/",
        BusTerminalListView.as_view(),
        name="bus_terminal_list",
    ),
    path(
        "timetable/",
        BusTimeTableListView.as_view(),
        name="bus_time_table_list",
    ),
]
