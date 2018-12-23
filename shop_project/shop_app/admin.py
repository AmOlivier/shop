from django.contrib import admin
from shop_app.models import Product , Client, Maillot, Comment, Response,Question, CommentResponse
# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Maillot)
admin.site.register(Comment)
admin.site.register(Response)
admin.site.register(Question)
admin.site.register(CommentResponse)

