from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField(max_length=255, null=True, blank=True)
    backdrop_url = models.URLField(max_length=255, null=True, blank=True)
    user_score_percentage = models.FloatField()
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Celebrity(models.Model):
    name = models.CharField(max_length=255)
    profile_picture_url = models.URLField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField()
    popularity = models.FloatField()
    previous_popularity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment_text = models.TextField(max_length='255', )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.comment_text[:20]}..."

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.movie_id}"
