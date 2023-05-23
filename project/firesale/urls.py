from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('members/', views.get_members, name='members'),
    path('members/create/', views.create_member, name='create_member'),
    path('items/', views.get_items, name='items'),
    path('items/create/', views.create_item, name='create_item'),
]
