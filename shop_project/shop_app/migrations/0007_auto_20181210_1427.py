# Generated by Django 2.1.3 on 2018-12-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_remove_client_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profil_picture',
            field=models.ImageField(default='static/images/defaultpicture.jpeg', upload_to='static/images/profil_pictures/'),
        ),
    ]