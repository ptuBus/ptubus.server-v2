from rest_framework.generics import ListAPIView
from .models import TrainTerminal, TrainTimeTable
from .serializers import (
    TrainTerminalSerializer,
    TrainTimeTableSerializer,
)


class TrainTerminalListView(ListAPIView):
    queryset = TrainTerminal.objects.all()
    serializer_class = TrainTerminalSerializer


class TrainTimeTableListView(ListAPIView):
    queryset = TrainTimeTable.objects.all()
    serializer_class = TrainTimeTableSerializer
