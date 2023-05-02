from django.contrib import admin
from blog.models import Category, Blog


class AdminBlogPost(admin.ModelAdmin):
    model = Blog
    list_display = ("title", "author", "status", "category", "created_date", "datetime_publish")
    list_filter = ("title", "author", "status", )
    search_fields = ("title", )
    

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("name", "created_date", "updated_date")
    list_filter = ("created_date", "updated_date")
    search_fields = ("name", )



admin.site.register(Blog, AdminBlogPost)
admin.site.register(Category, CategoryAdmin)
