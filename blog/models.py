from django.db import models

from users.models import User


class Blog(models.Model):
    """
    Модель блога
    """
    title = models.CharField(
        max_length= 250,
        verbose_name='Заголовок',
        help_text='Укажите заголовок блога'
    )
    slug = models.CharField(
        max_length=250,
        verbose_name="slug",
        null=True,
        blank=True
    )
    content = models.TextField(
        verbose_name='Содержимое',
        help_text='Введите текст блога',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='blog/',
        verbose_name="Изображение",
        help_text='Загрузите изображение для блога',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Введите дату создания блога'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
        help_text='Отметьте, если блог опубликован'
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Просмотры',
        editable=False,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Создатель карточки блога',
        blank=True,
        null=True,
        related_name='blogs_users'  # related_name для получения всех блогов пользователя
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Blog, self).delete(*args, **kwargs)
