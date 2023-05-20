from django.contrib import admin
from django import forms
from .models import TourObject, Tour, StartPlace, PriceExclude, PriceInclude, Order
from ckeditor.widgets import CKEditorWidget



# @admin.register(Tour)
# class TourAdmin(admin.ModelAdmin):
#     fields = ('name', 'price', 'description', 'main_photo', 'start_place', 'plan', 'tour_objects', 'price_include', 'price_exclude', 'food', 'ticket', 'notes' )
#     list_display = ('name', 'url')

class MyModelAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    plan = forms.CharField(widget=CKEditorWidget(), required=False)
    food = forms.CharField(widget=CKEditorWidget(), required=False)
    ticket = forms.CharField(widget=CKEditorWidget(), required=False)
    notes = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Tour
        fields = ('name', 'price', 'description', 'main_photo', 'start_place', 'plan', 'tour_objects', 'price_include',
                  'price_exclude', 'food', 'ticket', 'notes')


class MyModelAdmin(admin.ModelAdmin):
    form = MyModelAdminForm


class MyModelAdminForm1(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = TourObject
        fields = ('name', 'photo', 'description')


class MyModelAdmin1(admin.ModelAdmin):
    form = MyModelAdminForm1


admin.site.register(Tour, MyModelAdmin)
admin.site.register(TourObject, MyModelAdmin1)
admin.site.register(StartPlace)
admin.site.register(PriceExclude)
admin.site.register(PriceInclude)
admin.site.register(Order)