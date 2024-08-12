from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class PasswordForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)


class UserUpdateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'avatar', 'country', )