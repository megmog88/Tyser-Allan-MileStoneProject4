# Generated by Django 3.0.5 on 2021-05-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_auto_20210429_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='different_sizes',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
