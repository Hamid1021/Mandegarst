from django.urls import path
from Pig_Game.views import play

app_name = "Pig_Game"

urlpatterns = [
    path("", play, name="play")
]
