from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author',  'published_date', 'published')
    list_filter = ('published', 'published_date')
    search_fields = ('author', 'email', 'content')
