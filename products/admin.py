from django.contrib import admin
from .models import Product
# from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

class ProductA(admin.ModelAdmin):
    # exclude = ('description', )
    list_display = ('name', 'num_stars', 'description')
    # list_filter = (('mfg_date', DateRangeFilter), 'description')
    search_fields = ['name']

# Register your models here.
# admin.site.register(Product, ProductA)
admin.site.register(Product)
admin.site.site_header = "DataFlair Django Tutorials"