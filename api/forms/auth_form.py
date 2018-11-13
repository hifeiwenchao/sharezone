from django import forms


class PostLoginForm(forms.Form):
    http_methods = ('POST',)
    phone = forms.CharField(max_length=16, min_length=11)
    password = forms.CharField(min_length=6)
