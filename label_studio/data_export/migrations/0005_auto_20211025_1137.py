# Generated by Django 3.1.13 on 2021-10-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('data_export', '0004_auto_20211019_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='title',
            field=models.CharField(
                blank=True, default='', max_length=2048, verbose_name='title'
            ),
        ),
    ]
