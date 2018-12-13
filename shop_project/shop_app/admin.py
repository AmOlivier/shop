from django.contrib import admin
from shop_app.models import Product , Client, Maillot, Comment
# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Maillot)
admin.site.register(Comment)
