from django import forms
from .models import SaleCount

class ActivateForm(forms.ModelForm):
    class Meta:
        model = SaleCount
        fields = 'agent', 'salecount'
