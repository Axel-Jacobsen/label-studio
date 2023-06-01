# Generated by Django 3.1.14 on 2022-03-19 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhook',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                help_text='Creation time',
                verbose_name='created at',
            ),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='is_active',
            field=models.BooleanField(
                db_index=True,
                default=True,
                help_text='If value is False the webhook is disabled',
                verbose_name='is webhook active',
            ),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='send_for_all_actions',
            field=models.BooleanField(
                db_index=True,
                default=True,
                help_text='If value is False - used only for actions from WebhookAction',
                verbose_name='Use webhook for all actions',
            ),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='send_payload',
            field=models.BooleanField(
                db_index=True,
                default=True,
                help_text='If value is False send only action',
                verbose_name='does webhook send the payload',
            ),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='updated_at',
            field=models.DateTimeField(
                auto_now=True,
                db_index=True,
                help_text='Last update time',
                verbose_name='updated at',
            ),
        ),
        migrations.AlterField(
            model_name='webhookaction',
            name='action',
            field=models.CharField(
                choices=[
                    ['PROJECT_CREATED', 'Project created'],
                    ['PROJECT_UPDATED', 'Project updated'],
                    ['PROJECT_DELETED', 'Project deleted'],
                    ['TASKS_CREATED', 'Task created'],
                    ['TASKS_DELETED', 'Task deleted'],
                    ['ANNOTATION_CREATED', 'Annotation created'],
                    ['ANNOTATION_UPDATED', 'Annotation updated'],
                    ['ANNOTATIONS_DELETED', 'Annotation deleted'],
                    ['LABEL_LINK_CREATED', 'Label link created'],
                    ['LABEL_LINK_UPDATED', 'Label link updated'],
                    ['LABEL_LINK_DELETED', 'Label link deleted'],
                ],
                db_index=True,
                help_text='Action value',
                max_length=128,
                verbose_name='action of webhook',
            ),
        ),
    ]
