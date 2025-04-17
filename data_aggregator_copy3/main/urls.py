from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('api/current-time/', views.show_time, name='current_time'),
    path('api/current-price/', views.show_price, name='current_price'),
    path('api/checked-time/', views.latest_time, name='latest_time'),
]