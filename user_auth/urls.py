# user_auth/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('superuser/', include('items.urls')),
    path("accounts/<slug:slug>", views.slug_detail, name = "slug-detail-page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)