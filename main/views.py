from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tour, StartPlace, TourObject, PriceInclude, PriceExclude
from django_filters.views import FilterView
from .filtersets import TourFilter
from django.core.paginator import Paginator


def main_page(request):
    return render(request, 'base.html', context={})


class TourList(FilterView):
    model = Tour
    context_object_name = 'tours'
    filterset_class = TourFilter
    template_name = 'catalog.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tour_objects'] = TourObject.objects.all()
        context['start_places'] = StartPlace.objects.all()
        context['price_include'] = PriceInclude.objects.all()
        context['price_exclude'] = PriceExclude.objects.all()
        filtered_data = context['filter'].qs
        paginator = Paginator(filtered_data, self.paginate_by)
        page = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page)
        return context


class TourDetail(DetailView):
    model = Tour
    slug_url_kwarg = 'pk'
    template_name = 'tour_detail.html'
    context_object_name = 'tour'


def about_us(request):
    return render(request, 'about_us.html', context={})


def contacts(request):
    return render(request, 'contacts.html', context={})


def faq(request):
    return render(request, 'faq.html', context={})