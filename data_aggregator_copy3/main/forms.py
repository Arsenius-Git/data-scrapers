from django import forms
from .models import Get_stock
class Show_stock(forms.ModelForm):
    class Meta:
        model = Get_stock
        fields = ['stock']
        widgets = {
            'stock': forms.TextInput(attrs={'placeholder':'Enter here...'})
        }
class Stocks(forms.Form):
    stock = forms.CharField(max_length=20)