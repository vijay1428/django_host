# Generated by Django 4.1.7 on 2023-07-07 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_customuser_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentvisit',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recentvisit', to='products.productsupdate'),
        ),
    ]
