from django.urls import path, include
from . import views
from .views import Another

urlpatterns = [
    path('', views.home),
    path('p1/', views.page1),
    path('p2/', Another.as_view())
]