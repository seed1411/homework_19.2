from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'images', 'category', 'price')
    success_url = reverse_lazy('catalog:product_views')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'images', 'category', 'price')
    success_url = reverse_lazy('catalog:product_views')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_views')


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}({phone}) - {message}")
        return render(request, "catalog/contacts.html")








