from django.urls import path, include

urlpatterns = [
    path("subway/", include("ptu_subway.urls")),
    path("train/", include("ptu_train.urls")),
]
