from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('members/', views.get_members, name='members'),
    path('create_member/', views.create_member, name='create_member'),
    path('create_item/', views.create_item, name='create_item'),
]
