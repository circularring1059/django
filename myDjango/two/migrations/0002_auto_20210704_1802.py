# Generated by Django 2.2 on 2021-07-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': '车', 'verbose_name_plural': '车'},
        ),
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=8, verbose_name='carName'),
        ),
    ]
