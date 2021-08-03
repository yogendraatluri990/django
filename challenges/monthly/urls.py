# import statement
from django.urls import path

# import local statement
from . import views

urlpatterns = [
    path("", views.list_of_months, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="monthly-challenge"),    
]
