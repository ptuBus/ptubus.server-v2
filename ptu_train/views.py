from rest_framework.generics import ListAPIView

from .filters import TrainTerminalFilterBackend, TrainTimeTableFilterBackend
from .models import TrainTerminal, TrainTimeTable
from .serializers import (
    TrainTerminalSerializer,
    TrainTimeTableSerializer,
)


class TrainTerminalListView(ListAPIView):
    queryset = TrainTerminal.objects.all()
    serializer_class = TrainTerminalSerializer
    filter_backends = (TrainTerminalFilterBackend,)


class TrainTimeTableListView(ListAPIView):
    queryset = TrainTimeTable.objects.all()
    serializer_class = TrainTimeTableSerializer
    filter_backends = (TrainTimeTableFilterBackend,)
