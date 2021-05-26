from rest_framework.generics import ListAPIView
from .models import BusTerminal, BusTimeTable
from .serializers import BusTerminalSerializer, BusTimeTableSerializer
from .filters import BusTerminalFilterBackend, BusTimeTableFilterBackend


class BusTerminalListView(ListAPIView):
    queryset = BusTerminal.objects.all()
    serializer_class = BusTerminalSerializer
    filter_backends = (BusTerminalFilterBackend,)


class BusTimeTableListView(ListAPIView):
    queryset = BusTimeTable.objects.all()
    serializer_class = BusTimeTableSerializer
    filter_backends = (BusTimeTableFilterBackend,)
