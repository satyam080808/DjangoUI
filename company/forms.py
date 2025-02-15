from django import forms
from .models import CompanyVarity

class CompanyVarityForm(forms.Form):
    company_varity = forms.ModelChoiceField(queryset=CompanyVarity.objects.all(), label="Select company Variety")

    