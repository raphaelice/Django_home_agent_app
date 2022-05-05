from django.contrib import admin
from core import models


class ImageModelAdmin(admin.StackedInline):
    model = models.Image

class HouseModelAdmin(admin.ModelAdmin):
    inlines = [ImageModelAdmin]
    list_display = ('name', 'location')

admin.site.register(models.House, HouseModelAdmin)
admin.site.register(models.Location)
admin.site.register(models.Style)
admin.site.site_header = "Dinel's Agency"