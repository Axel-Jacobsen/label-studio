# Generated by Django 3.2.16 on 2023-04-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('data_export', '0009_alter_convertedformat_traceback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convertedformat',
            name='export_type',
            field=models.CharField(max_length=64),
        ),
    ]
