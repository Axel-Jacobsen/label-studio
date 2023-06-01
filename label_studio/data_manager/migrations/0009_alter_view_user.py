# Generated by Django 3.2.16 on 2023-03-10 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_manager', '0008_manual_counters_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='user',
            field=models.ForeignKey(
                help_text='User who made this view',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='data_manager_views',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
