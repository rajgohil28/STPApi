# Generated by Django 3.2.8 on 2021-12-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('ph', models.CharField(max_length=10)),
                ('temp', models.CharField(max_length=10)),
                ('BOD', models.CharField(max_length=10)),
                ('COD', models.CharField(max_length=10)),
                ('TSS', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('DO', models.CharField(max_length=10)),
                ('watercons', models.CharField(max_length=10)),
                ('Alkalinity', models.CharField(max_length=10)),
                ('EBOD', models.CharField(max_length=10)),
                ('ETSS', models.CharField(max_length=10)),
                ('ENH', models.CharField(max_length=10)),
                ('ANO', models.CharField(max_length=10)),
                ('Eph', models.CharField(max_length=10)),
                ('FMLSS', models.CharField(max_length=10)),
                ('ADO', models.CharField(max_length=10)),
                ('ANH', models.CharField(max_length=10)),
            ],
        ),
    ]
