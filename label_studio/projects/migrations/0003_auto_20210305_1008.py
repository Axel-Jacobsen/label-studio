# Generated by Django 3.1.4 on 2021-03-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0002_auto_20210304_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='enable_empty_completion',
            new_name='enable_empty_annotation',
        ),
        migrations.AlterField(
            model_name='project',
            name='enable_empty_annotation',
            field=models.BooleanField(
                default=True,
                help_text='Allow submit empty annotations',
                verbose_name='enable empty annotation',
            ),
        ),
        migrations.RenameField(
            model_name='project',
            old_name='maximum_completions',
            new_name='maximum_annotations',
        ),
        migrations.AlterField(
            model_name='project',
            name='maximum_annotations',
            field=models.IntegerField(
                default=1,
                help_text='Maximum overlaps of expert annotations for one task. If the annotation number per task is equal or greater to this value, the task becomes finished (is_labeled=True)',
                verbose_name='maximum annotation number',
            ),
        ),
        migrations.RenameField(
            model_name='project',
            old_name='min_completions_to_start_training',
            new_name='min_annotations_to_start_training',
        ),
        migrations.AlterField(
            model_name='project',
            name='min_annotations_to_start_training',
            field=models.IntegerField(
                default=10,
                help_text='Minimum number of completed tasks after which training is started',
                verbose_name='min_annotations_to_start_training',
            ),
        ),
        migrations.RenameField(
            model_name='project',
            old_name='show_completion_history',
            new_name='show_annotation_history',
        ),
        migrations.AlterField(
            model_name='project',
            name='show_annotation_history',
            field=models.BooleanField(
                default=False,
                help_text='Show annotation history to collaborator',
                verbose_name='show annotation history',
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='result_count',
            field=models.IntegerField(
                default=0,
                help_text='Total results inside of annotations counter',
                verbose_name='result count',
            ),
        ),
    ]
