# Generated by Django 4.2 on 2023-04-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_tour_description_alter_tour_food_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceExclude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='В вартість туру не входить')),
            ],
        ),
        migrations.CreateModel(
            name='PriceInclude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='В вартість туру входить')),
            ],
        ),
        migrations.RemoveField(
            model_name='tour',
            name='price_exclude',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='price_include',
        ),
        migrations.AddField(
            model_name='tour',
            name='price_exclude',
            field=models.ManyToManyField(blank=True, to='main.priceexclude', verbose_name='У вартість туру не входить'),
        ),
        migrations.AddField(
            model_name='tour',
            name='price_include',
            field=models.ManyToManyField(blank=True, to='main.priceinclude', verbose_name='У вартість туру входить'),
        ),
    ]
