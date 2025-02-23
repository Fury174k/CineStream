from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('room/<int:id>', views.roomPage, name="room"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('genre/<int:genre_id>', views.genrePage, name="genre_movies"),
    path('celebrity/<int:id>/', views.celebrity_profile, name='celebrity_profile'),
    path('add_to_watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
]