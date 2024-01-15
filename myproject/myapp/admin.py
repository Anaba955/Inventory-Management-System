from django.contrib import admin
from .models import features
from .models import Racks
from .models import Items

# Register your models here.
admin.site.register(features)
admin.site.register(Racks)
admin.site.register(Items)

# class RacksAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')  # Add the fields you want to display as columns

# admin.site.register(Racks, RacksAdmin)