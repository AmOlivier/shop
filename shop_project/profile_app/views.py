from django.shortcuts import render
from profile_app.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.


def signup(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)

	return render(request,'signup.html', context={'signup_form': SignupForm()})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)


	return render(request,'login.html', context={'login_form': LoginForm()})

def profile(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		

	return render(request,'profile.html', context={'login_form': LoginForm()})


	
