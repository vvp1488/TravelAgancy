# Generated by Django 4.2 on 2023-04-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='tour_objects',
            field=models.ManyToManyField(blank=True, to='main.tourobject', verbose_name="Екскурсійні об'єкти"),
        ),
    ]
