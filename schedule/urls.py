from django.urls import path

from . import views

urlpatterns = [
    path('', views.getSchedules),
    # path('getCustomer/<int:pk>/', views.getCustomer),
    # path('createCustomer/', views.createCustomer),
    # path('updateCustomer/<int:pk>/', views.updateCustomer),
    # path('deleteCustomer/<int:pk>/', views.deleteCustomer),
]