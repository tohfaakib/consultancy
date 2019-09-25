from django.contrib import admin
from .models import Slider, SliderText

class SliderAdmin(admin.ModelAdmin):
    fields = ('title', 'slider_image',)
    list_display = ('title', 'slider_image')


class SliderTextAdmin(admin.ModelAdmin):
    fields = ('title', 'message',)
    list_display = ('title', 'message')


admin.site.register(Slider, SliderAdmin)
admin.site.register(SliderText, SliderTextAdmin)