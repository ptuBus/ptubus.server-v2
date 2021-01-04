from rest_framework.permissions import (
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from ptu_subway.serializer import SubwayLineSerializer
from ptu_subway import get_line_data


class CrawlingSubwayLineData(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, **kwargs):
        line_data = get_line_data(
            "select LINE_NAME,LINE_CODE,LINE_COLOR_CODE, GUGTOBU_LINE_NAME from LINE_DATA WHERE AREA_CD='CA'"
        )

        serializer = SubwayLineSerializer(
            data=line_data,
            many=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"SubwayLine": "데이터가 DB에 의하여 생성되었습니다."},
        )
