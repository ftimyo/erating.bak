from django.contrib import admin
from .models import GreenMerchants

# Register your models here.
@admin.register(GreenMerchants)
class GreenMerchantsAdmin(admin.ModelAdmin):
    fields = ('mid','mname','mcat','mreward')
    list_display = ('mname','mreward')
