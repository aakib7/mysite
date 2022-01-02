from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    # that feild present in the form
    class Meta: # meta
        # model which we are going to use
        model = Item  
        # field which we want in our form
        fields = ['item_name', 'item_description','item_price','item_img']  
    
    
