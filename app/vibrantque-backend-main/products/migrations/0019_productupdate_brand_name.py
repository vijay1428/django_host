# Generated by Django 4.1.7 on 2023-05-20 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_productupdate_customer_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='productupdate',
            name='brand_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]