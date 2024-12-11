from django.urls import path
from application.views import (
    home, single_game, all_games, online_game_all,
    online_game_one, online_game_tow, online_game_three, 
)

app_name = "application"

urlpatterns = [
    path("", home, name="home"),
    path('game/<int:game_id>/<str:game_name>', single_game, name='single_game'),
    path('games/', all_games, name='all_games'),
    path('online_game_all/', online_game_all, name='online_game_all'),
    path('online_game_one/', online_game_one, name='online_game_one'),
    path('online_game_tow/', online_game_tow, name='online_game_tow'),
    path('online_game_three/', online_game_three, name='online_game_three'),
]
