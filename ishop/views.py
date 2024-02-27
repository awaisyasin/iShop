from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms

# Create your views here.

def home_view(request):
    return render(request, 'ishop/home.html')


class ShopCreateView(LoginRequiredMixin, CreateView):
    model = models.Shop
    form_class = forms.ShopCreateForm
    template_name = 'ishop/shop_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ShopDetailView(DetailView):
    model = models.Shop
    context_object_name = 'shop'