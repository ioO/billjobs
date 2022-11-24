# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billjobs', '0003_billline_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='issuer_address',
            field=models.CharField(default='\n            Your Coworking Space Name<br/>Building name<br/>\n            Number & Street<br/>Postal Code Town\n            ', max_length=1024),
        ),
        migrations.AlterField(
            model_name='billline',
            name='note',
            field=models.CharField(blank=True, help_text='Write a simple note which will be added in your bill', max_length=1024, verbose_name='Note'),
        ),
    ]
