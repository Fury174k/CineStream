from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('room/<int:id>/', views.roomPage, name="room"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('genre/<int:genre_id>/', views.genrePage, name="genre_movies"),
    path('celebrity/<int:id>/', views.celebrity_profile, name='celebrity_profile'),
    path('wishlist', views.watchlistPage, name="watchlist"),
    path('add_to_watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('search/', views.searchMovie, name='search'),
    path('top_movies/', views.getTop50movies, name='top-50-movies'),
    path('save_comment/', views.save_comment, name='save_comment'),
    path('pricing/', views.pricingPage, name='pricing'),
    path('clear_recently_viewed/', views.clear_recently_viewed, name='clear_recently_viewed'),
]