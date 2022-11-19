from django.urls import path

from . import views

urlpatterns = [
    path('', views.getSchedules),
    path('createSchedule/', views.createSchedule),
    # path('updateCustomer/<int:pk>/', views.updateCustomer),
    # path('deleteCustomer/<int:pk>/', views.deleteCustomer),
]