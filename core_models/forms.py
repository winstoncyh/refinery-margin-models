from django import forms
from .models import RefineryProcessUnit,RefinedProduct


class RefinedProduct(forms.ModelForm):
    class Meta:
        model = RefineryProcessUnit
        fields = [
            'refinedproduct_id',
            'name',
            'specific_gravity'
        ]
