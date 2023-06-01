# Generated by Django 3.1.13 on 2021-10-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ml', '0004_auto_20210820_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlbackend',
            name='is_interactive',
            field=models.BooleanField(
                default=False,
                help_text='Used to interactively annotate tasks. If true, model returns one list with results',
                verbose_name='is_interactive',
            ),
        ),
        migrations.AlterField(
            model_name='mlbackend',
            name='timeout',
            field=models.FloatField(
                blank=True,
                default=100.0,
                help_text='Response model timeout',
                verbose_name='timeout',
            ),
        ),
        migrations.AlterField(
            model_name='mlbackendpredictionjob',
            name='model_version',
            field=models.TextField(
                blank=True,
                help_text='Model version this job is associated with',
                null=True,
                verbose_name='model version',
            ),
        ),
    ]
