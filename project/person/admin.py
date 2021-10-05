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
    list_display = ("id", "date", "status", "status_code", )

    def get_readonly_fields(self, request, obj):
        return [field_.name for field_ in self.model._meta.fields]        

admin.site.register(User, CustomUserAdmin)
admin.site.register(RequestResult, RequestResultAdmin)
