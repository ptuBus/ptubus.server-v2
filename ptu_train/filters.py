from rest_framework.filters import BaseFilterBackend

from .serializers import TrainTerminalFilterSerializer, TrainTimeTableFilterSerializer


class TrainTerminalFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.GET:
            return queryset

        serializer = TrainTerminalFilterSerializer(
            context={
                "queryset": queryset,
                "request": request,
            },
            data=request.GET,
        )
        serializer.is_valid(raise_exception=True)

        if station_name := serializer.validated_data.get("station_name"):
            queryset = queryset.filter(
                end_station_name__contains=station_name,
            )

        return queryset


class TrainTimeTableFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.GET:
            return queryset

        serializer = TrainTimeTableFilterSerializer(
            context={
                "queryset": queryset,
                "request": request,
            },
            data=request.GET,
        )
        serializer.is_valid(raise_exception=True)

        if terminal_id := serializer.validated_data.get("terminal_id"):
            queryset = queryset.filter(train_terminal__end_terminal_id=terminal_id)
        elif rail_name := serializer.validated_data.get("rail_name"):
            queryset = queryset.filter(rail_name=rail_name)
        elif train_class := serializer.validated_data.get("train_class"):
            queryset = queryset.filter(train_class=train_class)
        elif daily_type_code := serializer.validated_data.get("daily_type_code"):
            queryset = queryset.filter(daily_type_code=daily_type_code)

        return queryset
