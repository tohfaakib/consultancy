from django.contrib import admin
from .models import Services

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Services, ServicesAdmin)

