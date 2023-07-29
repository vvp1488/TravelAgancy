from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView
from .models import Tour, StartPlace, TourObject, PriceInclude, PriceExclude, Order
from django_filters.views import FilterView
from .filtersets import TourFilter
from django.core.paginator import Paginator
from .forms import OrderForm
from django.contrib import messages
import requests


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
        context['form'] = OrderForm(self.request.GET)
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


def order_view(request, pk):
    if request.method == 'POST':
        tour = Tour.objects.get(pk=pk)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        order, created = Order.objects.get_or_create(name=name, surname=surname, phone=phone, tour=tour)
        info = request.POST.get('info')
        data = {
            "name": f"{name} {surname}",
            "phone": phone,
            "data": tour.name,
        }
        if info:
            order.info = info
            order.save()
            data["comment"] = info
        if email:
            data["email"] = email
        if created:
            messages.success(request, "Ваш запит успішно відправлено. Наш менеджер зв'яжеться з вами найближчим часом")
            url = 'https://api.allinclusivecrm.com/v1/site/api/create?access-token=8813161920-kfIatq_DjqirNdfT7fPwYq2MyoL1uWa9cDn0X5Eqyk7G9LxSsLG94VCCHhyu6EBaoAokiYlr6bPF2rDj8TCdyD6x6GCR0EBb9I1G'
            response = requests.post(url, json=data)
        else:
            messages.success(request, "Заявка була вже залишена. Наш менеджер зв'яжеться з вами найближчим часом")
    return redirect('catalog')
