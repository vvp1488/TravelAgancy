from django.contrib import admin
from .models import TourObject, Tour, StartPlace, PriceExclude, PriceInclude



@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'description', 'main_photo', 'start_place', 'plan', 'tour_objects', 'price_include', 'price_exclude', 'food', 'ticket', 'notes' )
    list_display = ('name', 'url')


admin.site.register(TourObject)
admin.site.register(StartPlace)
admin.site.register(PriceExclude)
admin.site.register(PriceInclude)