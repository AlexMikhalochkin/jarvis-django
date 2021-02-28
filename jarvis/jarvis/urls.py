from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('smartthings/', include('jarvis_api.urls')),
    path('admin/', admin.site.urls),
]
