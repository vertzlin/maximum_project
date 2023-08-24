from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date', 'updated_date','auction']
    list_filter = ['created_at', 'auction']
admin.site.register(Advertisements, AdvertisementAdmin)

# Register your models here.
