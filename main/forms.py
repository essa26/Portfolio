from django import forms


class SendEmail(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    message = forms.Textarea()

