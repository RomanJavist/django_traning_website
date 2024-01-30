# Generated by Django 5.0.1 on 2024-01-28 23:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_statuscrm_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_text', models.TextField(verbose_name='Comment text')),
                ('coment_dt', models.DateTimeField(auto_now=True, verbose_name='Creation date')),
                ('coment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Application')),
            ],
        ),
    ]
