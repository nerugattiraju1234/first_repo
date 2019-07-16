from django import forms
from django.contrib.auth.models import User

# Create your models here.
class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email","first_name","last_name"]
