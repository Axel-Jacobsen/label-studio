# Generated by Django 3.1.13 on 2021-09-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0008_auto_20210903_1332'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='annotation',
            index=models.Index(
                fields=['was_cancelled'], name='task_comple_was_can_f87d4e_idx'
            ),
        ),
        migrations.AddIndex(
            model_name='annotation',
            index=models.Index(
                fields=['ground_truth'], name='task_comple_ground__088a1b_idx'
            ),
        ),
        migrations.AddIndex(
            model_name='annotation',
            index=models.Index(
                fields=['created_at'], name='task_comple_created_f55e6f_idx'
            ),
        ),
    ]
