from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stuff)
admin.site.register(Supplier)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Client)
admin.site.register(Post)