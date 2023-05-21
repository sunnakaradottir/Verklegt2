from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('upload/', views.upload_data, name='upload'),
    path('success/', views.success_view, name='success'),
]