# Generated by Django 3.2.16 on 2023-03-23 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('data_export', '0005_auto_20211025_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertedFormat',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('file', models.FileField(null=True, upload_to='export')),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('created', 'Created'),
                            ('in_progress', 'In progress'),
                            ('failed', 'Failed'),
                            ('completed', 'Completed'),
                        ],
                        default='created',
                        max_length=64,
                    ),
                ),
                (
                    'export_type',
                    models.CharField(
                        choices=[
                            ('created', 'Created'),
                            ('in_progress', 'In progress'),
                            ('failed', 'Failed'),
                            ('completed', 'Completed'),
                        ],
                        default='created',
                        max_length=64,
                    ),
                ),
                (
                    'export',
                    models.ForeignKey(
                        help_text='Export snapshot for this converted file',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='converted_formats',
                        to='data_export.export',
                    ),
                ),
            ],
        ),
    ]
