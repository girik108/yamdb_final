from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "text", "score", "pub_date")


admin.site.register(Review, ReviewAdmin)
