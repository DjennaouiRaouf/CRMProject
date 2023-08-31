from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

lpp=20

class CustomUserAdmin(UserAdmin):
    list_display = ['user_id','username','phone_number','email','is_active','otp_enabled']
    list_per_page = lpp
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email','phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('2FA', {'fields': ('otp_enabled','otp_base32','otp_auth_url')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    actions = ['activate_user', 'deactivate_user','disable_otp']



    def activate_user(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_user(self, request, queryset):
        queryset.update(is_active=False)

    def disable_otp(self, request, queryset):
        queryset.update(otp_enabled=False,otp_base32=None,otp_auth_url=None)

admin.site.register(UserAccount, CustomUserAdmin)


class CustomGroupAdmin(GroupAdmin):
    list_display = ['group_id','name']
    pass

admin.site.unregister(Group)
admin.site.register(GroupUser, CustomGroupAdmin)
