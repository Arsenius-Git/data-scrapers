from django import forms
from django.contrib.auth.forms import User, UserCreationForm
from .models import create_model, looking_for_offers

class CreateOffer(forms.ModelForm):
    class Meta:
        model = create_model
        fields = ['job_name','min_experience','company_name','requirements']
        widgets ={
            'job_name': forms.TextInput(attrs={'placeholder':'Enter a job position...'}),
            'min_experience':forms.TextInput(attrs={'placeholder':'Enter a min experience time you expect..'}),
            'company_name':forms.TextInput(attrs={'placeholder':'Enter a company name...'}),
            'requirements':forms.TextInput(attrs={'placeholder':'Enter requirements'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LookingForOffer(forms.ModelForm):
    class Meta:
        model = looking_for_offers
        fields = ['job_name', 'experience','abilities']
        widgets = {
            'job_name':forms.TextInput(attrs={'placeholder':"Enter job you're looking for"}),
            'experience':forms.TextInput(attrs={'placeholder':"Enter your past job experiences"}),
            'abilities':forms.TextInput(attrs={'placeholder':"Enter your abilities"})
        }
