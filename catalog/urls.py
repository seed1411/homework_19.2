from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, ContactView, CategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_views"),
    path("product/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/create/", never_cache(ProductCreateView.as_view()), name="product_create"),
    path("product/<int:pk>/update/", never_cache(ProductUpdateView.as_view()), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

    path("contacts/", ContactView.as_view(), name="contacts"),

    path("product/category/view", CategoryListView.as_view(), name="category_list"),

]
