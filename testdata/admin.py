from django.contrib import admin

# Register your models here.
import models

class DataAdmin(admin.ModelAdmin):
	list_display = ('path', 'name')

admin.site.register(models.Data, DataAdmin)
