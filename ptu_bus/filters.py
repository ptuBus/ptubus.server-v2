from rest_framework.filters import BaseFilterBackend

from .serializers import BusTerminalFilterSerializer, BusTimeTableFilterSerializer


class BusTerminalFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.GET:
            return queryset

        serializer = BusTerminalFilterSerializer(
            context={
                "queryset": queryset,
                "request": request,
            },
            data=request.GET,
        )
        serializer.is_valid(raise_exception=True)

        station_name = serializer.validated_data.get("station_name")
        is_express = serializer.validated_data.get("is_express")

        if station_name:
            queryset = queryset.filter(
                end_station_name__contains=station_name,
            )
        elif is_express:
            queryset = queryset.filter(
                is_express=is_express,
            )
        return queryset


class BusTimeTableFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.GET:
            return queryset

        serializer = BusTimeTableFilterSerializer(
            context={
                "queryset": queryset,
                "request": request,
            },
            data=request.GET,
        )
        serializer.is_valid(raise_exception=True)

        if station_id := serializer.validated_data.get("station_id"):
            return queryset.filter(bus_terminal__end_station_id=station_id)

        return queryset
