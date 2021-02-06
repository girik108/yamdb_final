from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "review", "text")


admin.site.register(Comment, CommentAdmin)
