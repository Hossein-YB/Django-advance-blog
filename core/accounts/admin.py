from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active", "last_login")
    list_filter = ("email", "is_superuser", "is_active")
    search_fields = ("email", )
    ordering = ("email", )
    readonly_fields = ("created_date", "updated_date",)
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
            'fields': ("created_date", "updated_date", "last_login", )
        }))
    
    add_fieldsets = (
        ("Create a new user", {
            'classes': ("wide", ),
            'fields': ("email", "password1", "password2", "is_staff",  "is_active", "is_superuser",)
        }), 
    )
    
    

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
    

admin.site.site_header = "Blog admin page"
admin.site.site_title = "Site management panel | admin panel"
admin.site.index_title = "Welcome to blog admin panel"