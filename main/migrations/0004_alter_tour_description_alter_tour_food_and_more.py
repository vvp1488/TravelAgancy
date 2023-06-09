# Generated by Django 4.2 on 2023-04-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tourobject_description_alter_tourobject_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(blank=True, verbose_name='Короткий опис туру'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='food',
            field=models.TextField(blank=True, verbose_name='Харчування'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Додаткова інформація'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='plan',
            field=models.TextField(blank=True, verbose_name='План туру'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price_exclude',
            field=models.TextField(blank=True, verbose_name='У вартість туру не входить'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price_include',
            field=models.TextField(blank=True, verbose_name='У вартість туру входить'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='ticket',
            field=models.TextField(blank=True, verbose_name='Вхідні квитки'),
        ),
        migrations.AlterField(
            model_name='tourobject',
            name='description',
            field=models.TextField(blank=True, verbose_name='Опис'),
        ),
    ]
