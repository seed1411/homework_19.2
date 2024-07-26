from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('created_at', 'is_published')
    search_fields = ('title', 'content')
