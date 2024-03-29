from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    path('log/<int:pk>/', views.log_details, name='log_detail'),
    path('log/new', views.log_new, name = 'log_new'),
]