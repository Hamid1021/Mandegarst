from django.contrib import admin

from .models import Game, Banner

class GameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'game_name', 'game_genre', 'rate_score', 'publish_status', 'is_deleted')
    list_filter = ('game_genre', 'publish_status', 'is_deleted')
    search_fields = ('game_name', 'game_description', 'text_link_win', 'text_link_ios', 'text_link_android')
    list_display_links = ('game_name', )

class BannerAdmin(admin.ModelAdmin):
    list_display = ('position', 'game', 'status')
    list_filter = ('status',)
    search_fields = ('position', 'game__game_name')
    list_display_links = ('position', 'game')


admin.site.register(Game, GameAdmin)
admin.site.register(Banner, BannerAdmin)
