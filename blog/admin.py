from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author',  'date_published', 'published')
    list_filter = ('published', 'date_published')
    search_fields = ('author', 'email', 'content')
