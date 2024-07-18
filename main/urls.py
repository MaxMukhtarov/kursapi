from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_list, name='currency-list'),
    path('create/', views.currency_create, name='currency-create'),
    path('edit/<int:pk>/', views.currency_edit, name='currency-edit'),
    path('delete/<int:pk>/', views.currency_delete, name='currency-delete'),
]

