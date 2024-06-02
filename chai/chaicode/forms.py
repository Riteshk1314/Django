from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
  chai_varity = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="Select Chai Variety")
  #since we have written choice field so it will take only dropdown objects