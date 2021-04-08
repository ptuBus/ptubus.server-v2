from rest_framework.generics import ListAPIView

from ptu_bus.models import BusTerminal
from ptu_bus.serializers import BusTerminalSerializer


class BusTerminalListView(ListAPIView):
    serializer_class = BusTerminalSerializer
    queryset = BusTerminal.objects.all()
