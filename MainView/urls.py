from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("View/Auth", views.auth_page),
    path("View/Profile", views.profile_page),
    path("View/single", views.fb_page_details)
]
