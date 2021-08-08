from django.urls import path


# importing views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard-page")
]
