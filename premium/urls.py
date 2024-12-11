from django.urls import path
from premium.views import *

app_name = "premium"

urlpatterns = [
    path("premium/", premium, name="premium"),
]
