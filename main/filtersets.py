import django_filters
from django_filters.widgets import RangeWidget, LookupChoiceWidget
from .models import Tour, StartPlace, TourObject, PriceInclude, PriceExclude
from django import forms


class MultiSelectWidget(forms.SelectMultiple):
    def __init__(self, attrs=None, choices=()):
        super(MultiSelectWidget, self).__init__(attrs)
        self.choices = choices


class TourFilter(django_filters.FilterSet):
    start_place = django_filters.ModelMultipleChoiceFilter(
        queryset=StartPlace.objects.all(),
        widget=MultiSelectWidget(attrs={'class': 'form-control'}),
    )
    price = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'class': 'form-control'})
    )
    tour_objects = django_filters.ModelMultipleChoiceFilter(
        queryset=TourObject.objects.all(),
        widget=MultiSelectWidget(attrs={'class': 'form-control'}),
    )
    price_include = django_filters.ModelMultipleChoiceFilter(
        queryset=PriceInclude.objects.all(),
        widget=MultiSelectWidget(attrs={'class': 'form-control'}),
    )
    price_exclude = django_filters.ModelMultipleChoiceFilter(
        queryset=PriceExclude.objects.all(),
        widget=MultiSelectWidget(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Tour
        fields = ['price', 'start_place', 'tour_objects', 'price_include', 'price_exclude']
