from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('members/', views.get_members, name='members'),
    path('create_member/', views.create_member, name='create_member'),
    path('create_item/', views.create_item, name='create_item'),
    path('item/<slug:item_id>/', views.item_information, name='item_information'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
