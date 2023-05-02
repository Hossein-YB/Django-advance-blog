from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active", "last_login")
    list_filter = ("email", "is_superuser", "is_active")
    search_fields = ("email", )
    ordering = ("email", )
    
    fieldsets = (
        ("authentication", {
            'fields': ("email", "password", )
            }  
        ),
        ("permissions", { 
            'fields': ("is_staff", "is_superuser", "is_active")
        }),
        ("group permissions", { 
            'fields': ("groups", "user_permissions", )
        }),
        ("important date", { 
            'fields': ("last_login", )
        }))
    
    add_fieldsets = (
        ("authentication", {
            'classes': ("wide", ),
            'fields': ("email", "password1", "password2", "is_staff", "is_superuser", "is_active")
        })
    )
    
    

admin.site.register(User, CustomUserAdmin)
    

