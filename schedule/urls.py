from django.urls import path

from . import views

urlpatterns = [
    path('', views.getSchedules),
    path('createSchedule/', views.createSchedule),
    path('updateSchedule/<int:pk>/', views.updateSchedule),
    path('deleteSchedule/<int:pk>/', views.deleteSchedule),
]