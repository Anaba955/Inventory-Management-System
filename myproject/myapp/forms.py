from django import forms
from .models import Items,features, Racks


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['id','name', 'Qty', 'box_id']
        # unique_together = (('name', 'id'),)
    
class BoxForm(forms.ModelForm):
    class Meta:
        model = features
        fields = ['id','name', 'Qty', 'rack_id']
        # unique_together = (('name', 'rack_id'),)
        

# class SearchForm(forms.Form):
#     class Meta:
#         model = Items
#         fields = [ 'name']


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100)  # Define the 'name' field directly in the form class

