from django import forms
from core.models import Events



# class AddEventForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Name of Event", "class": "form-control", "type":"text"}))
#     budget = forms.CharField(widget=forms.DecimalField(attrs={"placeholder":"Name of Event", "class": "form-control", "type":"text"}))


#     class Meta():
#         model = Events
#         fields = ['title']