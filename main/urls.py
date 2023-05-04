from django.urls import path
from .views import main_page, TourList, TourDetail, about_us, contacts, faq, order_view


urlpatterns = [
    path('', main_page, name='main_page'),
    path('catalog/', TourList.as_view(), name='catalog'),
    path('catalog/<int:pk>/', TourDetail.as_view(), name='detail_tour'),
    path('about-us/', about_us, name='about-us'),
    path('contacts/', contacts, name='contacts'),
    path('faq/', faq, name='faq'),
    path('order/', order_view, name='order')
]