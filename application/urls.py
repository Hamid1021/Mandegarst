from django.urls import path
from application.views import (
    home, single_game, all_games, online_game_all,
)

app_name = "application"

urlpatterns = [
    path("", home, name="home"),
    path('game/<int:game_id>/<str:game_name>', single_game, name='single_game'),
    path('games/', all_games, name='all_games'),
    path('online_game_all/', online_game_all, name='online_game_all'),
]
