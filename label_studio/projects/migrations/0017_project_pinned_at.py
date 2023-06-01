# Generated by Django 3.2.13 on 2022-07-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0016_auto_20220211_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pinned_at',
            field=models.DateTimeField(
                default=None,
                help_text='Pinned date and time',
                null=True,
                verbose_name='pinned at',
            ),
        ),
    ]
