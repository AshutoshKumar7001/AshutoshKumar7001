from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('p1/', views.page1)
]