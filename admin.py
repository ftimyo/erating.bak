from django.contrib import admin
from .models import GreenMerchants, GreenMerchantCat

# Register your models here.
@admin.register(GreenMerchants)
class GreenMerchantsAdmin(admin.ModelAdmin):
    fields = ('mid','mname','mcat','mreward')
    list_display = ('mname','mreward')

@admin.register(GreenMerchantCat)
class GreenMerchantsCatAdmin(admin.ModelAdmin):
    fields = ('catn',)
    list_display = ('catn',)
