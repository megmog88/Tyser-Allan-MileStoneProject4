# Generated by Django 3.0.5 on 2021-04-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draping', '0002_remove_drape_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='drape',
            name='cover',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
