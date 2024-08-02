from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if cleaned_data.lower() in forbidden_words:
            raise ValidationError('Имеется запрещенное слово, используете только разрешенные слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if cleaned_data.lower() in forbidden_words:
            raise ValidationError('Имеется запрещенное слово, используете только разрешенные слова')
        return cleaned_data

