from django.urls import path, include

urlpatterns = [
    path("subway/", include("ptu_subway.urls")),
    path("train/", include("ptu_train.urls")),
    path("school/", include("ptu_school.urls")),
    path("bus/", include("ptu_bus.urls")),
]
