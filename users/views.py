import secrets
import string
import random


from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, PasswordForm, UserUpdateForm
from users.models import User


class UserRegisterView(CreateView):
    """
    Регистрация нового пользователя с подтверждением почты
    и генерацией токена подтверждения
    """
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        host = self.request.get_host()
        token = secrets.token_hex(16)
        user.token = token
        user.save(update_fields=['token', 'is_active'])
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            "Подтверждение почты",
            f'Пройдите по ссылке для подтверждения почты {url}',
            EMAIL_HOST_USER,
            [user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    """
    Перевод пользователя в статуc Активный при проходе по ссылке с почты
    """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save(update_fields=['is_active'])
    return redirect(reverse('users:login'))


class GeneratePasswordView(PasswordResetView):
    """
    Генерация пароля при нажатии на кнопку "Восстановить пароль"
    c генерируемым новым паролем
    """
    model = User
    form_class = PasswordForm
    template_name = "users/recover_password.html"
    success_url = reverse_lazy("users/login.html")

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = get_object_or_404(User, email=email)
        symbols = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        random.shuffle(symbols)
        new_password = "".join(symbols[:13])
        user.set_password(new_password)
        user.save()
        send_mail(
            "Сброс пароля",
            f'Ваш новый пароль: {new_password}',
            EMAIL_HOST_USER,
            [user.email]
        )
        return redirect(reverse('users:login'))


class ProfileDetailView(DetailView):
    """
    Вывод информации о пользователе
    """
    model = User


class ProfileUpdateView(UpdateView):
    """
    Вывод формы редактирования профиля пользователя
    """
    model = User
    form_class = UserUpdateForm

    def get_success_url(self):
        """
        Возвращает URL для перехода на детальную страницу пользователя после успешного редактирования
        """
        return reverse('users:profile', kwargs={'pk': self.object.pk})

