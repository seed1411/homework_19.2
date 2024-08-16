from django.forms import ModelForm

from blog.models import Blog


class BlogFrom(ModelForm):
    """
    Форма для создания и редактирования публикации блога
    """
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'is_published')

