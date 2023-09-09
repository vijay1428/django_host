# Generated by Django 4.1.7 on 2023-04-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_addcartupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ImageField(max_length=1000, upload_to='Product')),
                ('user_name', models.CharField(blank=True, max_length=250)),
                ('customer_review', models.CharField(blank=True, max_length=256)),
                ('client_review', models.CharField(blank=True, max_length=25)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]