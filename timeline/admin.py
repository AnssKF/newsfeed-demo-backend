from django.contrib import admin
import nested_admin

from .models import *


#-- Post
class PostCommentAdminInline(nested_admin.NestedStackedInline):
    model = Comment
    extra = 0
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Post)
class PostAdmin(nested_admin.NestedModelAdmin):
    def likes(self, obj):
        return obj.likes.count()
    likes.short_description = "Likes Count"

    search_fields = ['author', 'content', 'created_at', ]
    list_display = ['author', 'content', 'created_at', 'likes']
    list_filter = ('author', 'content', 'created_at', )
    inlines = [PostCommentAdminInline]

    # TODO: Uncomment
    # readonly_fields = ['author', 'content', 'created_at', 'updated_at', ]
    # def has_add_permission(self, request, obj=None):
    #     return False


#-- Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['author', 'content', 'post', 'created_at', ]
    list_display = ['author', 'content', 'post', 'created_at', ]
    list_filter = ('author', 'content', 'post', 'created_at', )

    # TODO: Uncomment
    # readonly_fields = ['author', 'content', 'post', 'created_at', 'updated_at', ]
    # def has_add_permission(self, request, obj=None):
    #     return False

# TODO: Delete
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = ['author', 'post', ]
    list_display = ['author', 'post', ]
    list_filter = ('author', 'post', )

