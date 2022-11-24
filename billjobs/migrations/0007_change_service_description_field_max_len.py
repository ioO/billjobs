# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billjobs', '0006_add_billin_address_and_migrate_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(help_text='Write service description limited to 256 characters', max_length=256, verbose_name='Description'),
        ),
    ]
