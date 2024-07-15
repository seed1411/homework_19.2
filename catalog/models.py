from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    images = models.ImageField(
        upload_to="product/",
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена",
        help_text="введите цену на единицу товара",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату записи в базу данных",
        blank=True,
        null=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
        blank=True,
        null=True,
    )
    manufactured_at = models.DateField(
        verbose_name='Дата производства продукта',
        help_text='Введите дату производства',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name
