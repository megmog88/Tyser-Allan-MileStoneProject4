# Generated by Django 3.0.5 on 2021-04-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landscaping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landscape',
            name='cover',
            field=models.ImageField(upload_to='', verbose_name='media/images/'),
        ),
    ]
