from django.urls import path

from . import views

urlpatterns = [
    path('', views.getEmployees),
    path('getEmployee/<int:pk>/', views.getEmployee),
    path('createEmployee/', views.createEmployee),
    path('updateEmployee/<int:pk>/', views.updateEmployee),
    path('deleteEmployee/<int:pk>/', views.deleteEmployee),
]