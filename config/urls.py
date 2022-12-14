from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('food/', include('food.urls')),
    path('lifestyle/', include('lifestyle.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)