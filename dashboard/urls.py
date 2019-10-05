from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name='index'),
    path('logging_in/', views.logging_in, name='logging_in'),
    path('logging_out/', views.logging_out, name='logging_out'),
    path('dashboard/', views.dashboard, name='dashboard')
]