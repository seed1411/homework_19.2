from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Админка модели Blog
    """
    list_display = ('title', 'is_published', 'owner')
    list_filter = ('created_at', 'is_published')
    search_fields = ('title', 'content')
