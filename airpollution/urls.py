from django.urls import path
from airpollution import views

app_name = 'airpollution'
urlpatterns = [
    path('', views.welcome, name='welcome'),
]
