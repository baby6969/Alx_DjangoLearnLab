from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # make sure this is imported

# Custom admin for the CustomUser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register the model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
