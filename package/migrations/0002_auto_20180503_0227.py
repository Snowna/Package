# Generated by Django 2.0.5 on 2018-05-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='staff_company',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='package',
            name='staff_price',
            field=models.CharField(default='', max_length=100),
        ),
    ]
