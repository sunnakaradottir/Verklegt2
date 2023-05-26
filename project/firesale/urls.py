from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('members/', views.get_members, name='members'),
    path('create_member/', views.create_member, name='create_member'),
    path('create_item/', views.create_item, name='create_item'),
    path('item/<slug:item_id>/', views.item_information, name='item_information'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('items/bid/<int:item_id>/', views.create_bid, name="create_bid"),
    path('profile/', views.profile, name='profile'),
    path('items/bids/<int:item_id>/', views.view_bids, name='view_bids'),
    path('items/bids/<int:item_id>/<int:bid_id>/', views.accept_bid, name='accept_bid'),
    path('items/bids/<int:item_id>/<int:bid_id>/', views.reject_bid, name='reject_bid')
]