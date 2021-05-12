from rest_framework.generics import ListAPIView
from .models import SchoolBusTimeTable
from .serializers import SchoolBusTimeTableSerializer


class SchoolBusTimeTableListView(ListAPIView):
    queryset = SchoolBusTimeTable.objects.all()
    serializer_class = SchoolBusTimeTableSerializer
