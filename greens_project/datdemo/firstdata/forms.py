from django import forms


class student(forms.Form):
    username = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    phonenumber = forms.CharField(max_length=100)