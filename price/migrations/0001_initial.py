# Generated by Django 5.0.1 on 2024-01-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Price')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Service')),
                ('pt_old_price', models.CharField(max_length=200, verbose_name='Old price')),
                ('pt_new_price', models.CharField(max_length=200, verbose_name='New price')),
            ],
        ),
    ]