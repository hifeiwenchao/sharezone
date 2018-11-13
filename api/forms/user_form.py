from django import forms


class GetProfileForm(forms.Form):
    http_methods = ('GET',)
    uid = forms.IntegerField(min_value=1)

