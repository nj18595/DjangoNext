from django.urls import path
from items import views

urlpatterns = [
    path('add_item/', views.add_item, name='add_item'),
    path('home/', views.home, name='home'),
]
