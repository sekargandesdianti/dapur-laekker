from django.forms import ModelForm
from main.models import Inventory

class ProductForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "amount", "description"]