from dataclasses import field
from distutils.command.upload import upload
from django import forms
from .models import Customers

class DateInput(forms.DateInput):
    input_type = 'date'
class CustomersForms(forms.ModelForm):
    data = forms.DateTimeField(widget=DateInput)
    image = forms.ImageField()
    class Meta:
        model = Customers
        fields = "__all__"



