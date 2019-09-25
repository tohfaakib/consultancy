from django.contrib import admin
from .models import About, FAQ

class AboutAdmin(admin.ModelAdmin):
    pass
    # list_display = ('title', 'slider_image')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(About, AboutAdmin)
admin.site.register(FAQ, FAQAdmin)
