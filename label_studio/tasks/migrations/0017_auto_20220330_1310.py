# Generated by Django 3.1.14 on 2022-03-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0016_auto_20220414_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='total_annotations',
            field=models.IntegerField(
                db_index=True,
                default=0,
                help_text='Number of total annotations for the current task',
                verbose_name='total_annotations',
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='cancelled_annotations',
            field=models.IntegerField(
                db_index=True,
                default=0,
                help_text='Number of total cancelled annotations for the current task',
                verbose_name='cancelled_annotations',
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='total_predictions',
            field=models.IntegerField(
                db_index=True,
                default=0,
                help_text='Number of total predictions for the current task',
                verbose_name='total_predictions',
            ),
        ),
    ]
