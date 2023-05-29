from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Item)
admin.site.register(models.ItemImage)
admin.site.register(models.Category)
admin.site.register(models.Location)
admin.site.register(models.Bid)
admin.site.register(models.Message)
admin.site.register(models.Contact)
admin.site.register(models.Payment)
admin.site.register(models.Order)