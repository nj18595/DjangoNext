from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['appname', 'applink', 'category1', 'category2', 'add_points']

    # Optional: Add custom widgets for better UI (e.g., for the dropdowns)
    category1 = forms.ChoiceField(choices=Item.CATEGORY_CHOICES_1)
    category2 = forms.ChoiceField(choices=Item.CATEGORY_CHOICES_2)
