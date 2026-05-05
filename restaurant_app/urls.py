from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('index/', views.home, name='index'),
    
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='book'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_items, name='menu_item'),
]
