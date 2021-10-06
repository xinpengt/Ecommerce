

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Cart, Product,Category,Account,Comment,Cart,Order,OrderProduct
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AccountName(admin.ModelAdmin):
    list_display=['username']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Account,AccountName)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderProduct)
