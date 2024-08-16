from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogFrom
from blog.models import Blog


class BlogListView(ListView):
    """
    Выводит список всех публикаций блога
    """
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """
        Получает все публикации блога, которые опубликованы
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    """
    Выводит конкретную публикацию блога с подробным описанием и картинкой
    """
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save(update_fields=['views_count'])
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Выводит страницу для создания новой публикации блога
    """
    model = Blog
    form_class = BlogFrom
    success_url = reverse_lazy('blog:blog_views')

    def form_valid(self, form):
        """
        Проверяет данные на валидность и генерирует слаг
        """
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.owner = self.request.user
            new_mat.save(update_fields=['slug', 'owner'])
        return super().form_valid((form))


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Выводит страницу для редактирования конкретной публикации блога
    """
    model = Blog
    form_class = BlogFrom
    success_url = reverse_lazy('blog:blog_views')

    def get_success_url(self):
        """
        Возвращает URL страницы с детальным описанием публикации блога
        """
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """
    Выводит страницу для удаления конкретной публикации блога
    """
    model = Blog
    success_url = reverse_lazy('blog:blog_views')
