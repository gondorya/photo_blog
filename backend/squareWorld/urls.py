from django.conf import settings
from django.urls import path, include
from blog.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('getData/', get_data),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
