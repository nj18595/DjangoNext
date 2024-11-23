from django import forms
from items.models import Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['appname', 'applink', 'category1', 'category2', 'add_points', 'logo']

    # Optional: Add custom widgets for better UI (e.g., for the dropdowns)
    category1 = forms.ChoiceField(choices=Item.CATEGORY_CHOICES_1)
    category2 = forms.ChoiceField(choices=Item.CATEGORY_CHOICES_2)
    # logo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))  # Customize the file input for the logo


class SignUpFormAdmin(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginFormAdmin(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
