from django.urls import path, include

urlpatterns = [
    path("subway/", include("ptu_subway.urls")),
    path("bus/", include("ptu_bus.urls")),
]
