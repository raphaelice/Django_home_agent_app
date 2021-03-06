from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]