from django.urls import path
from . import views

app_name = 'profile_app'


urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('profile/', views.profile, name='profile'),

  ]