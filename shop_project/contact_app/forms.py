from django import forms
from contact_app.models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['subject','email','description']
		widgets = {
		'subject':forms.TextInput(attrs={
			'id':'subject-contact',
			'placeholder':'subject',
			'required':True
			}),		
		'email':forms.EmailInput(attrs={
			'id':'email-contact',
			'placeholder':'Write you email here ...',
			'required':True
			}),
		'description':forms.Textarea(attrs={
			'id':'description-contact',
			'placeholder':'Write a comment here ...',
			'required':True
			}),
		}

	