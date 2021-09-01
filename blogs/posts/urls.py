from django.urls import path


# importing views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard-page"),
    path("posts", views.allPosts, name="posts-page"),
    path("post/<slug:slug>", views.blogDetail, name="blog-detail-page")
]
