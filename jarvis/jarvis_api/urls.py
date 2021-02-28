from django.urls import path

from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('token/', views.token, name='token'),
    path('', views.handle, name='handle'),
]
