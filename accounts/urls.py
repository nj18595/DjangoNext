# accounts/urls.py
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.list_items, name='user_home'),
    path('upload/', views.ImageUploadView.as_view(), name='image-upload'),
    path('item_detail/<int:item_id>/', views.item_detail, name='item_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
