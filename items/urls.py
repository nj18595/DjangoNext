from django.urls import path
from items import views

urlpatterns = [
    path('signup/', views.signup, name='admin_signup'),
    path('login/', views.login_view, name='admin_login'),
    path('add_item/', views.add_item, name='add_item'),
    path('home/', views.home, name='home'),
]

