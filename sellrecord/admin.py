from django.contrib import admin
from .models import Sellrecord

admin.site.site_header = 'Mandalay Shweyi Showroon Sale Admin'

class SellrecordAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'purchased_items', 'price', 'showroon', 'paid', 'date']
    list_filter = ['customer_name', 'customer_phone', 'purchased_items', 'price', 'showroon', 'paid', 'date']
    search_fields = ['customer_name', 'customer_phone', 'purchased_items', 'price', 'showroon', 'paid', 'date']

admin.site.register(Sellrecord, SellrecordAdmin)