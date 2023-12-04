from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'date_of_birth', 'join_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email')

    def full_name(self, obj):
        return obj.full_name()

    full_name.short_description = 'Full Name'
