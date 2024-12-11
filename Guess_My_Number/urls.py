from django.urls import path
from Guess_My_Number.views import play

app_name = "Guess_My_Number"

urlpatterns = [
    path("", play, name="play")
]
