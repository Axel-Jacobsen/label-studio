# Generated by Django 3.1.13 on 2021-11-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0012_auto_20210906_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='reveal_preannotations_interactively',
            field=models.BooleanField(
                default=False,
                help_text='Reveal pre-annotations interactively',
                verbose_name='reveal_preannotations_interactively',
            ),
        ),
    ]
