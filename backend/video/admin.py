from django.contrib import admin

from video.models import Playlist, PlaylistVideo, Video, VideoCategory


class VideoCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(VideoCategory, VideoCategoryAdmin)


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Playlist, PlaylistAdmin)


class PlaylistVideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(PlaylistVideo, PlaylistVideoAdmin)
