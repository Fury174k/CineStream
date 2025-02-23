from django.contrib import admin
from .models import Room, Celebrity, Comment, Watchlist

# Register your models here.

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'room', 'date_created')
    search_fields = ('user__username', 'comment_text', 'room__title')

# If you have the Room model, you can also register it

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('tmdb_id', 'title', 'release_date', 'user_score_percentage')
    search_fields = ('title', 'tmdb_id')

admin.site.register(Celebrity)
admin.site.register(Watchlist)