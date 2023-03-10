from . import views
from django.urls import path

urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view())
]
