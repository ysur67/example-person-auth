from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from person.models import User, RequestResult


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            (None, {
                'fields': ('birth_date', 'phone', 'name')
                }),
    )

class RequestResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(RequestResult)
