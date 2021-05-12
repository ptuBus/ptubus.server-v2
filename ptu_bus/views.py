from rest_framework.generics import ListAPIView
from .models import BusTerminal, BusTimeTable
from .serializers import BusTerminalSerializer, BusTimeTableSerializer


class BusTerminalListView(ListAPIView):
    queryset = BusTerminal.objects.all()
    serializer_class = BusTerminalSerializer


class BusTimeTableListView(ListAPIView):
    queryset = BusTimeTable.objects.all()
    serializer_class = BusTimeTableSerializer
