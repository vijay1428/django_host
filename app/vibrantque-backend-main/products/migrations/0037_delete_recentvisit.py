# Generated by Django 4.2.4 on 2023-08-02 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_delete_orderdelivery'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecentVisit',
        ),
    ]