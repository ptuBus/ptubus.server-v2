from rest_framework.permissions import (
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    SubwayLine,
    SubwayStation,
)
from .serializers import (
    SubwayLineSerializer,
    SubwayStationSerializer,
)
from . import (
    get_line_data,
    get_station_data,
)


class CrawlingSubwayLineData(APIView):
    permission_classes = [IsAdminUser]
    queryset = SubwayLine.objects.all()

    def get(self, request, **kwargs):
        self.queryset.delete()

        line_data = get_line_data(
            "select LINE_NAME,LINE_CODE,LINE_COLOR_CODE, GUGTOBU_LINE_NAME from LINE_DATA WHERE AREA_CD='CA'"
        )

        serializer = SubwayLineSerializer(
            data=line_data,
            many=True,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"SubwayLine": "데이터가 DB에 의하여 생성되었습니다."},
        )


class CrawlingSubwayStationData(APIView):
    permission_classes = [IsAdminUser]
    queryset = SubwayStation.objects.all()

    def get(self, request, **kwargs):
        self.queryset.delete()

        station_data = get_station_data()

        serializer = SubwayStationSerializer(
            data=station_data,
            many=True,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"SubwayStation": "데이터가 CSV에 의하여 생성되었습니다."},
        )
