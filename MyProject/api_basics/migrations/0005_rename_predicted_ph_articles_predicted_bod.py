# Generated by Django 3.2.8 on 2021-12-21 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0004_auto_20211221_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='predicted_ph',
            new_name='predicted_BOD',
        ),
    ]
