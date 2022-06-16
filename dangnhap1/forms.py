from django import forms
    # TODO: Define form fields here
class signupForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(max_length=25)
