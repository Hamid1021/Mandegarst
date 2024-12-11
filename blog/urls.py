from django.urls import path
from blog.views import Blogs, single_blog

app_name = "blog"

urlpatterns = [
    path("blogs", Blogs, name="HomeBlogs"),
    path("posts/<int:pk>/<slug:slug>/", single_blog, name="single_blog"),
]
