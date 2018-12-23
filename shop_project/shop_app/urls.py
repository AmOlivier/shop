from django.urls import path
from . import views

app_name = 'shop_app'


urlpatterns = [
  path('', views.index, name='index'),
  path('products/<int:product_id>/', views.product, name='product'),
  path('clients/', views.clients, name='clients'),
  path('clients/<int:client_id>/', views.client, name='client'),
  path('maillots/', views.maillots, name='maillots'),
  path('maillots/<int:maillot_id>/', views.maillot, name='maillot'),
  path('products/<int:product_id>/comment_form', views.comment_form, name='comment_form'),
  path('products/<int:product_id>/question_form', views.question_form, name='question_form'),
  path('questions/<int:question_id>/responseform', views.responseform, name='responseform'),
  path('comments/<int:comment_id>/commentresponseform', views.commentresponseform, name='commentresponseform'),

  
]