# Generated by Django 3.2.8 on 2021-12-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0002_auto_20211219_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='predicted_ph',
            field=models.FloatField(default=0.0, max_length=10),
        ),
    ]