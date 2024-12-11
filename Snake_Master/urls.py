from django.urls import path
from Snake_Master.views import (
    play, death, keep, limitless, sneak, watch, difficulty, difficultyDefault, instruction, 
)

app_name = "Snake_Master"

urlpatterns = [
    path("", play, name="play"),
    path("death", death, name="death"),
    path("keep", keep, name="keep"),
    path("limitless", limitless, name="limitless"),
    path("sneak", sneak, name="sneak"),
    path("watch", watch, name="watch"),
    path("difficulty", difficulty, name="difficulty"),
    path("difficultyDefault", difficultyDefault, name="difficultyDefault"),
    path("instruction", instruction, name="instruction"),
]
