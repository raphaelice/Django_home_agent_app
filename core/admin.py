from django.contrib import admin
from core import models


class ImageModelAdmin(admin.StackedInline):
    model = models.Image

class HouseModelAdmin(admin.ModelAdmin):
    inlines = [ImageModelAdmin]

admin.site.register(models.Image)
admin.site.register(models.House, HouseModelAdmin)
admin.site.register(models.Location)