from django.urls import path

from . import views

app_name='gestion_doublons'
urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
]