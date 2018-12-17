# Generated by Django 2.1.3 on 2018-12-09 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_auto_20181209_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=264, unique=True)),
                ('profil_picture', models.ImageField(default='static/images/ecran.png', upload_to='static/images/profil_pictures/')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.Product')),
            ],
        ),
    ]
