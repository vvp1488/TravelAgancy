# Generated by Django 4.2 on 2023-04-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_priceexclude_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Вартість'),
        ),
    ]
