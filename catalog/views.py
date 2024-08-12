from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    """
    Вывод списка всех продуктов
    """
    model = Product


class ProductDetailView(DetailView):
    """
    Вывод детальной страницы продукта
    """
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Вывод формы создания нового продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_views')

    def form_valid(self, form):
        product = form.save()
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Вывод формы редактирования продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_views')

    def get_success_url(self):
        """
        Возвращает URL для перехода на детальную страницу продукта после успешного редактирования
        """
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        """
        Добавляет форму версии продукта к контексту
        """
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """
        Проверка формы и формы версии на правильность заполнения
        """
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            versions = Version.objects.filter(product=self.object, current_version_flag=True)
            if len(versions) > 1:
                form.add_error(None, 'У продукта не может быть более одной активной версии.')
                return super().form_invalid(form)
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Вывод формы удаления продукта
    """
    model = Product
    success_url = reverse_lazy('catalog:product_views')


class ContactView(TemplateView):
    """
    Вывод страницы контактов
    """
    template_name = "catalog/contacts.html"

    def post(self, request):
        """
        Отправка POST запроса с формы контактов

        """
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}({phone}) - {message}")
        return render(request, "catalog/contacts.html")








