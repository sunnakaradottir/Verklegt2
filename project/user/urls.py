from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", LoginView.as_view(template_name='user/login.html'), name="login"),
    path("logout", LogoutView.as_view(next_page='login'), name="logout"),
    path("profile", views.profile, name="profile"),
    path("inbox", views.inbox, name="inbox"),
    path("listings", views.my_listings, name="listings"),
    path("favorites", views.favorites, name="favorites"),
    path("orders", views.orders, name="orders"),
    path('user/inbox/delete/<int:bid_id>/', views.delete_offer, name='delete_offer'),
    path('reviews', views.my_reviews, name='reviews'),
]