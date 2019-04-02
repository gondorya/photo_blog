from django.urls import path, include
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('new_post/', views.new_post, name='new_post'),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]