from django import forms
from .models import Items,features

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['id','name', 'Qty', 'box_id']
    
class BoxForm(forms.ModelForm):
    class Meta:
        model = features
        fields = ['id','name', 'Qty', 'rack_id']

