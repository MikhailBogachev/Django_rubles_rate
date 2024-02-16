from django.contrib import admin

from .models import RublesRate


class RublesRateAdmin(admin.ModelAdmin):
    list_display = ('id', 'charcode', 'date', 'rate')
    list_editable = ('charcode', 'date', 'rate')
    list_filter = ('charcode', 'date')


admin.site.register(RublesRate, RublesRateAdmin)
