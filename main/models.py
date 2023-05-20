from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse


class TourObject(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=100)
    photo = models.FileField(verbose_name='Фото', upload_to='tour_objects_photo/', blank=True)
    description = models.TextField(verbose_name='Опис', blank=True)

    class Meta:
        verbose_name = "Екскурсійний об'єкт"
        verbose_name_plural = "Екскурсійні об'єкти"

    def __str__(self):
        return self.name


class StartPlace(models.Model):
    name = models.CharField(verbose_name='Місце посадки', max_length=100, db_index=True)

    class Meta:
        verbose_name = "Місце посадки"
        verbose_name_plural = "Місця посадки"

    def __str__(self):
        return self.name


class PriceInclude(models.Model):
    name = models.CharField(verbose_name='В вартість туру входить', max_length=150, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тур вкючає"
        verbose_name_plural = "Тур вкючає"


class PriceExclude(models.Model):
    name = models.CharField(verbose_name='В вартість туру не входить', max_length=150, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тур не вкючає"
        verbose_name_plural = "Тур не вкючає"



class Tour(models.Model):

    name = models.CharField(verbose_name='Назва туру', max_length=100, unique=True)
    price = models.DecimalField(verbose_name='Вартість', max_digits=10, decimal_places=2,  blank=True, null=True)
    description = models.TextField(verbose_name='Короткий опис туру',  blank=True)
    main_photo = models.FileField(verbose_name='Головне фото', blank=True, upload_to='tour_main_photo/')
    start_place = models.ManyToManyField(StartPlace, verbose_name='Місце посадки',  blank=True)
    plan = models.TextField(verbose_name='План туру', blank=True)
    tour_objects = models.ManyToManyField(TourObject, verbose_name="Екскурсійні об'єкти", blank=True)
    price_include = models.ManyToManyField(PriceInclude, verbose_name='У вартість туру входить', blank=True)
    price_exclude = models.ManyToManyField(PriceExclude, verbose_name='У вартість туру не входить', blank=True)
    food = models.TextField(verbose_name='Харчування', blank=True)
    ticket = models.TextField(verbose_name='Вхідні квитки', blank=True)
    notes = models.TextField(verbose_name='Додаткова інформація', blank=True)
    url = models.SlugField(max_length=160, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Тури"
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_tour', kwargs={'pk': self.pk})


class Order(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=50, null=True, blank=True)
    surname = models.CharField(verbose_name='Прізвище', max_length=60, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=9)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    info = models.TextField(verbose_name="Додаткова інформація", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'{self.name} - {self.surname} : {self.phone}'


@receiver(pre_save, sender=Tour)
def generate_slug(sender, instance, **kwargs):
    if not instance.url:
        instance.url = slugify(instance.name)