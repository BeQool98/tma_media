from django import forms

class MessageForm(forms.Form):
    name=forms.CharField(max_length=200)
    email=forms.EmailField(max_length=200)
    phone=forms.CharField(max_length=200)
    comment = forms.CharField(widget=forms.Textarea)   