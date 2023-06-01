# Generated by Django 3.2.16 on 2022-12-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0033_annotation_updated_by_fill'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='annotation',
            name='task_comple_last_cr_dedad7_idx',
        ),
        migrations.RemoveIndex(
            model_name='task',
            name='task_is_labe_215a18_idx',
        ),
        migrations.AlterField(
            model_name='annotation',
            name='ground_truth',
            field=models.BooleanField(
                default=False,
                help_text='This annotation is a Ground Truth (ground_truth)',
                verbose_name='ground_truth',
            ),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='was_cancelled',
            field=models.BooleanField(
                default=False,
                help_text='User skipped the task',
                verbose_name='was cancelled',
            ),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_labeled',
            field=models.BooleanField(
                default=False,
                help_text='True if the number of annotations for this task is greater than or equal to the number of maximum_completions for the project',
                verbose_name='is_labeled',
            ),
        ),
    ]
