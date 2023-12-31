from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control','rows': 4}))
