from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('', views.login, name='login'),
    ]