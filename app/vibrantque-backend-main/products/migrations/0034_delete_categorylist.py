# Generated by Django 4.2.4 on 2023-08-02 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_delete_rateupdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoryList',
        ),
    ]