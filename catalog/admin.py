from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Админка модели Category
    """
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админка модели Product
    """
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """
    Админка модели Version
    """
    list_display = ("id", "number_version", "current_version_flag", "product")
    list_filter = ("product",)
    search_fields = ("number_version",)
