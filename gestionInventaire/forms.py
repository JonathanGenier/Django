from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

# Form d'un produit (Pour ADD et EDIT)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'product_type', 'price', 'current_quantity', 'stock_quantity')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input '}),
            'description': forms.TextInput(attrs={'class': 'form-input '}),
            'product_type': forms.TextInput(attrs={'class': 'form-input '}),
            'price': forms.NumberInput(attrs={'class': 'form-input '}),
            'current_quantity': forms.NumberInput(attrs={'class': 'form-input '}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-input'}),
        }

# Form permettant un utilisateur de s'authentifier
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input '}),
            'password': forms.PasswordInput(attrs={'class': 'form-input '}),
        }

# Form permettant un utilisateur de s'enregistrer
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input '}),
            'email': forms.TextInput(attrs={'class': 'form-input '}),
            'first_name': forms.TextInput(attrs={'class': 'form-input '}),
            'last_name': forms.TextInput(attrs={'class': 'form-input '}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input '}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input '}),
        }


