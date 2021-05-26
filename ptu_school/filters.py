from rest_framework.filters import BaseFilterBackend

from ptu_school.serializers import SchoolBusTimeTableFilterSerializer


class SchoolBusTimeTableFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if not request.GET:
            return queryset

        serializer = SchoolBusTimeTableFilterSerializer(
            context={
                "queryset": queryset,
                "request": request,
            },
            data=request.GET,
        )
        serializer.is_valid(raise_exception=True)
        queryset = queryset.filter(
            up_down_type_code=serializer.validated_data.get("way"),
        )
        return queryset
