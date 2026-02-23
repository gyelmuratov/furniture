from django.contrib import admin

from blogs.models import Author, Category, Tag, Blog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'is_active' , 'created_at']
    search_fields = ['full_name','professions']
    list_filter = ['created_at', 'updated_at', 'is_active','professions' ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at']
    search_fields = ['title', 'short_description', 'long_description']
    list_filter = ['authors', 'categories', 'tags', 'status', 'created_at', 'updated_at']





