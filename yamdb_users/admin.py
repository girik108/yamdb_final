from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "role", "is_superuser")
    search_fields = ("username",)
    list_filter = ("role",)
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
