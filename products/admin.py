from django.contrib import admin
from products.models import Category,Manufacturer,Color,Tag,Product,ProductImage


admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductImage)
