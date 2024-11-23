# accounts/urls.py
from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.list_items, name='user_home'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
]
