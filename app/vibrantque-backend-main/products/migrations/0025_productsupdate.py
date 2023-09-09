# Generated by Django 4.1.7 on 2023-05-26 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_orderdelivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ImageField(max_length=1000, upload_to='Product')),
                ('offer', models.CharField(blank=True, max_length=25)),
                ('price', models.CharField(blank=True, max_length=256)),
                ('discount', models.CharField(blank=True, max_length=25)),
                ('brand_name', models.CharField(blank=True, max_length=256)),
                ('shipping_mode', models.CharField(blank=True, max_length=256)),
                ('product_name', models.CharField(blank=True, max_length=256)),
                ('product_description', models.CharField(blank=True, max_length=250)),
                ('customer_rate', models.CharField(blank=True, max_length=256)),
                ('post_type', models.CharField(blank=True, max_length=25)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productsupdate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]