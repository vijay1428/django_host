# Generated by Django 4.1.7 on 2023-06-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_categorylist_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
