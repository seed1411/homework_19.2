import json
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_categories() -> list:
        """
        Получение данных из фикстуры с категориями
        :return: список с категориями
        """
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog.json"), encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_products() -> list:
        """
        Получение данных из фикстуры с продуктами
        :return: список с продуктами
        """
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog.json"), encoding="utf-8") as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == "catalog.product"]
        return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Category.truncate_table_restart_id()

        category_for_create = []
        products_for_create = []

        for category in Command.json_categories():
            category_for_create.append(Category(**category['fields']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_products():
            products_for_create.append(Product(
                name=product['fields']['name'],
                description=product['fields']['description'],
                images=product['fields']['images'],
                category=Category.objects.get(pk=product['fields']['category']),
                price=product['fields']['price'],
                created_at=product['fields']['created_at'],
                updated_at=product['fields']['updated_at']
            ))

        Product.objects.bulk_create(products_for_create)





