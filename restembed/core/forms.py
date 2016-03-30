from django import forms

class SubmitEmbed(forms.Form):
    url = forms.URLField()


def clean_url(self):
		print (self.cleaned_data)
		url = self.cleaned_data['url']
		return url


