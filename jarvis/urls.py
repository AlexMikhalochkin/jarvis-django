from django.urls import include, path

urlpatterns = [
    path('smartthings/', include('jarvis_api.urls'))
]
