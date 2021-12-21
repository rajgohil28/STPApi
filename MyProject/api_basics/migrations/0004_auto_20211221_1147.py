# Generated by Django 3.2.8 on 2021-12-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0003_articles_predicted_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Alkalinity',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='articles',
            name='BOD',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='COD',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='EBOD',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='ETSS',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='FMLSS',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='watercons',
            field=models.FloatField(max_length=10),
        ),
    ]
