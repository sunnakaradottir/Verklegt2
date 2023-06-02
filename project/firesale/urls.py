from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", include("user.urls")),
    path('create_item/', views.create_item, name='create_item'),
    path('item/<slug:item_id>/', views.item_information, name='item_information'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('items/bid/<int:item_id>/', views.create_bid, name="create_bid"),
    path('profile/', views.profile, name='profile'),
    path('items/bids/<int:item_id>/', views.view_bids, name='view_bids'),
    path('items/bids/<int:item_id>/<int:bid_id>/', views.accept_bid, name='accept_bid'),
    path('filter/<slug:category_id>/', views.filtered_categories, name='filtered_categories'),
    path('index/', views.index, name='index_search'),
    path('sort/', views.sort_items, name='sort_items'),
    path('checkout/<int:message_id>/<int:bid_id>/<string:back>/', views.contact_info, name='contact_info'),
    path('checkout/<int:message_id>/<int:bid_id>/<int:contact_id>/', views.payment_info, name='payment_info'),
    path('checkout/<int:message_id>/<int:bid_id>/<int:contact_id>/<int:payment_id>/', views.rating_seller, name='rating_seller'),
    path('checkout/<int:message_id>/<int:bid_id>/<int:contact_id>/<int:payment_id>/<int:order_id>/<int:review_id>/', views.order_review, name='order_review'),
    path('pages/about/', views.about_page, name='about'),
    path('pages/terms/', views.terms_page, name='terms'),
    path('pages/faq/', views.faq_page, name='faq'),
    path('pages/contact/', views.contact_page, name='contact'),
]