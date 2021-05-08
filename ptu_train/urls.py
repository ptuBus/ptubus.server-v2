from django.urls import path

from ptu_train.views import TrainTerminalListView, TrainTimeTableListView

urlpatterns = [
    path(
        "terminal/",
        TrainTerminalListView.as_view(),
        name="train_terminal_list",
    ),
    path(
        "timetable/",
        TrainTimeTableListView.as_view(),
        name="train_time_table_list",
    ),
]
