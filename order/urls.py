from django.urls import path

from . import views

urlpatterns = [
    path('', views.getOrders),
    path('getOrder/<int:pk>/', views.getOrder),
    path('createOrder/', views.createOrder),
    path('updateOrder/<int:pk>/', views.updateOrder),
    path('deleteOrder/<int:pk>/', views.deleteOrder),
]