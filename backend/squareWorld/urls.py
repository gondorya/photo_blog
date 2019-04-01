from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getData/', get_data),
    path('', TemplateView.as_view(template_name="home.html"), name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
