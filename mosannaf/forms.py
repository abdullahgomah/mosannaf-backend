from .models import Rate
from django import forms 

class RateForm(forms.ModelForm): 

    class Meta:
        model = Rate 
        fields = ['details']