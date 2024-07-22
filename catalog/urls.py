from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, prod_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>", prod_detail, name="prod_detail"),
]
