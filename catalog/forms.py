from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    """
    Mixin для стилизации формы.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    """
    Форма добавления и редактирования продукта.
    """
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']

    @staticmethod
    def valid_text(text):
        """
        Проверка текста на наличие запрещенных слов.
        """
        edited_text = text.lower().strip(' ,.!:" ').replace('.', '').replace(',', '').split()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in edited_text:
            if word in forbidden_words:
                raise ValidationError('Имеется запрещенное слово, используете только разрешенные слова')
        else:
            return text

    def clean_name(self):
        """
        Проверка названия продукта на наличие запрещенных слов.
        """
        return self.valid_text(self.cleaned_data['name'])

    def clean_description(self):
        """
        Проверка описания продукта на наличие запрещенных слов.
        """
        return self.valid_text(self.cleaned_data['description'])


class VersionForm(StyleFormMixin, ModelForm):
    """
    Форма добавления и редактирования версии продукта.
    """
    class Meta:
        model = Version
        fields = '__all__'






