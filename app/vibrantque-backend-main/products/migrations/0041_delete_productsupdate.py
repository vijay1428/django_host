# Generated by Django 4.2.4 on 2023-08-02 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_delete_route'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductsUpdate',
        ),
    ]