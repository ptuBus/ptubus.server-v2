from django.urls import path

from ptu_school.views import SchoolBusTimeTableListView

urlpatterns = [
    path(
        "timetable/",
        SchoolBusTimeTableListView.as_view(),
        name="school_bus_time_table_list",
    ),
]
