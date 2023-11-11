from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('create_or_update/', views.Create_or_update, name='create_or_update'),
    path('delete/', views.Delete, name='delete'),
]
