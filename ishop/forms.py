from django import forms
from django.urls import reverse_lazy

from . import models


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = ['name', 'username', 'description', 'phone_number']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }
        success_url = reverse_lazy('ishop:shop_detail')