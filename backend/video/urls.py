from django.urls import include, path, re_path
from rest_framework import routers

from video.views import (
    PlaylistVideoViewSet,
    PlaylistViewSet,
    VideoCategoryViewSet,
    VideoUploadView,
    VideoViewSet,
)

router = routers.DefaultRouter()
router.register(r"category", VideoCategoryViewSet, basename="videocategory")
router.register(r"playlist/video", PlaylistVideoViewSet, basename="playlist-video")
router.register(r"playlist", PlaylistViewSet, basename="playlist")

router.register(r"", VideoViewSet, basename="video")


urlpatterns = [
    re_path(r"upload/(?P<filename>[^/]+)$", VideoUploadView.as_view()),
    # path('playlist/video', PlaylistVideoViewSet.as_view()),
    path("", include(router.urls)),
]
