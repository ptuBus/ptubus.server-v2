from rest_framework.generics import ListAPIView
from ptu_school.models import SchoolBusTimeTable
from ptu_school.serializers import SchoolBusTimeTableSerializer


class SchoolBusTimeTableListView(ListAPIView):
    queryset = SchoolBusTimeTable.objects.all()
    serializer_class = SchoolBusTimeTableSerializer
