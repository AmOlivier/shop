# Generated by Django 2.1.3 on 2018-12-10 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='products',
        ),
    ]