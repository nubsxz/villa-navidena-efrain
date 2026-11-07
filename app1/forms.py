from django import forms
from .models import Store

class newstoreform(forms.Form):
    name = forms.CharField(label="name", max_length=100, 
                           widget=forms.TextInput(attrs={'class':'textinp'}))
    description = forms.CharField(label="description", widget=forms.Textarea(attrs={'class':'textinp'}))


class newproductform(forms.Form):
    title = forms.CharField(label="title", max_length=100, 
     widget=forms.TextInput(attrs={'class':'textinp'}))
    price = forms.FloatField(label="price",
                             widget=forms.NumberInput(attrs={'class':'textinp'}))
    store = forms.ModelChoiceField(label="store", queryset=Store.objects.all(),
                                   widget=forms.Select(attrs={'class':'textinp'}))

class newcontactform(forms.Form):
    email=forms.CharField(label='Email', max_length=100, 
                          widget=forms.TextInput(attrs={'class':'textinp'}))
