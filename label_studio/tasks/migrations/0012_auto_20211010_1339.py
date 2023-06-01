# Generated by Django 3.1.13 on 2021-10-10 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0011_merge_20210914_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='parent_prediction',
            field=models.ForeignKey(
                help_text='Points to the prediction from which the annotation was created',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='child_annotations',
                to='tasks.prediction',
            ),
        ),
        migrations.AddField(
            model_name='annotation',
            name='parent_annotation',
            field=models.ForeignKey(
                help_text='Points to the parent annotation from which this annotation was created',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='child_annotations',
                to='tasks.annotation',
            ),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='parent_prediction',
            field=models.ForeignKey(
                help_text='Points to the prediction from which this annotation was created',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='child_annotations',
                to='tasks.prediction',
            ),
        ),
    ]
