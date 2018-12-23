from django.shortcuts import render , redirect
from contact_app.models import Contact
from contact_app.forms import ContactForm


def success(request):
	return render(request,'success.html')
# Create your views here.
def contact_form(request):
	if request.method == 'POST':
		subject = request.POST.get('subject')
		email = request.POST.get('email')
		description = request.POST.get('description')
		Contact.objects.get_or_create(subject=subject,email=email,description=description)


	

	contact_form = ContactForm()
	return render(request, "contact_form.html", context={'contact_form': contact_form })
