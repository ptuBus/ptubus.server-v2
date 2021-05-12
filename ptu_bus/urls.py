from django.urls import path

from .views import BusTerminalListView, BusTimeTableListView

urlpatterns = [
    path(
        "terminal/",
        BusTerminalListView.as_view(),
        name="train_terminal_list",
    ),
    path(
        "timetable/",
        BusTimeTableListView.as_view(),
        name="train_time_table_list",
    ),
]
