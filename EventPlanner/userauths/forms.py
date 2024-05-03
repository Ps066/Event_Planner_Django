from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username", "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "class": "form-control"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Phone no.", "class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password", "class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password", "class": "form-control"}))

    class Meta():
        model = User
        fields = ['username', 'email', 'phone']

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user   