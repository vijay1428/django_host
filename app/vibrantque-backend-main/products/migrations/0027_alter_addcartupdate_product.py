# Generated by Django 4.1.7 on 2023-05-28 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_productsupdate_process_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcartupdate',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addcartupdate', to='products.productsupdate'),
        ),
    ]