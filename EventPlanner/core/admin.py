from django.contrib import admin
from core.models import Product , Category , Vendor, CartOrder , CartOrderItems , ProductImages ,Events


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['pid','Product_name','user','image','price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_id','title','image']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['ven_id','title','image']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','image','quantity','item','price']

class EventAdmin(admin.ModelAdmin):
    list_display = ['eve_id','title','user','budget','category']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Events, EventAdmin)