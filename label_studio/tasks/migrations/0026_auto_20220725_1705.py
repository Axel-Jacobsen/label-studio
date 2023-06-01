# Generated by Django 3.1.14 on 2022-07-25 17:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0025_auto_20220721_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='last_action',
            field=models.CharField(
                choices=[
                    ('prediction', 'Created from prediction'),
                    ('propagated_annotation', 'Created from another annotation'),
                    ('imported', 'Imported'),
                    ('submitted', 'Submitted'),
                    ('updated', 'Updated'),
                    ('skipped', 'Skipped'),
                    ('accepted', 'Accepted'),
                    ('rejected', 'Rejected'),
                    ('fixed_and_accepted', 'Fixed and accepted'),
                    ('deleted_review', 'Deleted review'),
                ],
                default=None,
                help_text='Action which was performed in the last annotation history item',
                max_length=128,
                null=True,
                verbose_name='last action',
            ),
        ),
        migrations.AlterField(
            model_name='task',
            name='comment_authors',
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text='Users who wrote comments',
                related_name='tasks_with_comments',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
