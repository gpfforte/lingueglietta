from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from .models import Post, Comment

# admin.site.register(Post)
# admin.site.register(Comment)


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 1

# Register the Admin classes for Book using the decorator


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    date_hierarchy = "date_posted"
    list_filter = ('author', 'title')
    ordering = ('author', "date_posted",)
    raw_id_fields = ("author",)
    search_fields = ("content",)
    inlines = [CommentsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # def get_post_title(self, obj):
    #     return obj.post.title
    # get_post_title.short_description = "Post Title"
    list_display = ('content', 'author', 'post', 'date_modified')
    date_hierarchy = "date_published"
    list_filter = ('author', 'post')
    ordering = ('author', "date_published",)
    raw_id_fields = ("author",)
    search_fields = ("content",)

# class UserAdmin(admin.ModelAdmin):
#     def group(self, user):
#         groups = []
#         for group in user.groups.all():
#             groups.append(group.name)
#         return ' '.join(groups)
#     group.short_description = 'Groups'
#     list_display = ('username','email', 'first_name', 'last_name','group','is_staff','is_superuser')
#     list_filter = ('is_staff', 'is_superuser')

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
