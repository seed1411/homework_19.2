from django.db import models, connection


class Category(models.Model):
    """
    Модель категории продукта
    """
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

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )


class Product(models.Model):
    """
    Модель продукта
    """
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
        default=0,
        help_text="введите цену на единицу товара",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату записи в базу данных",
        blank=True,
        null=True,
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name

    @property
    def active_version(self):
        """
        Возвращает активную версию продукта в ListView
        """
        return self.versions.filter(current_version_flag=True).first()


class Version(models.Model):
    """
    Модель версии продукта
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Наименование продукта",
        help_text="Выберите продукт",
        related_name="versions",
    )
    number_version = models.FloatField(
        verbose_name="Номер версии",
        help_text="Введите номер версии продукта",
    )
    name_version = models.CharField(
        max_length=250,
        verbose_name="Название версии",
        help_text="Введите название версии продукта",
        null=True,
        blank=True,
    )
    current_version_flag = models.BooleanField(
        verbose_name="Текущая версия",
        help_text="Установите флаг текущей версии",
    )

    def __str__(self):
        return f'{self.number_version}'

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продуктов'
        ordering = ('number_version',)