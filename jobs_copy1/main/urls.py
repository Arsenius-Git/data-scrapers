from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('job_offers/', views.home, name='home'),
    path('create_offer/', views.create_offer, name='create_offer'),
    path('create_cv', views.create_cv, name='create_cv'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register')
]