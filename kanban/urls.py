from django.urls import path

from . import views

urlpatterns = [
    path('', views.getKanbans),
    path('createKanban/', views.createKanban),
    path('updateKanban/<int:pk>/', views.updateKanban),
    path('deleteKanban/<int:pk>/', views.deleteKanban),
]