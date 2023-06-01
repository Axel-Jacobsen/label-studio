# Generated by Django 3.1.14 on 2022-08-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0027_auto_20220801_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationdraft',
            name='lead_time',
            field=models.FloatField(
                blank=True,
                help_text='How much time it took to annotate the task',
                null=True,
                verbose_name='lead time',
            ),
        ),
    ]
