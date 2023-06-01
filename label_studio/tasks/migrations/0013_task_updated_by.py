# Generated by Django 3.1.14 on 2022-03-11 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0012_auto_20211010_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_by',
            field=models.ForeignKey(
                help_text='Last annotator or reviewer who updated this task',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='updated_tasks',
                to=settings.AUTH_USER_MODEL,
                verbose_name='updated by',
            ),
        ),
    ]
