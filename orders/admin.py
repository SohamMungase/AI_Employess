from django.contrib import admin
from .models import Product, Orders, RefundRequest

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(RefundRequest)
