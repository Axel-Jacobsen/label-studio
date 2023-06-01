# Generated by Django 3.1.13 on 2021-09-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('io_storages', '0006_auto_20210906_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='azureblobexportstorage',
            name='can_delete_objects',
            field=models.BooleanField(
                blank=True,
                help_text='Deletion from storage enabled',
                null=True,
                verbose_name='can_delete_objects',
            ),
        ),
        migrations.AddField(
            model_name='gcsexportstorage',
            name='can_delete_objects',
            field=models.BooleanField(
                blank=True,
                help_text='Deletion from storage enabled',
                null=True,
                verbose_name='can_delete_objects',
            ),
        ),
        migrations.AddField(
            model_name='localfilesexportstorage',
            name='can_delete_objects',
            field=models.BooleanField(
                blank=True,
                help_text='Deletion from storage enabled',
                null=True,
                verbose_name='can_delete_objects',
            ),
        ),
        migrations.AddField(
            model_name='redisexportstorage',
            name='can_delete_objects',
            field=models.BooleanField(
                blank=True,
                help_text='Deletion from storage enabled',
                null=True,
                verbose_name='can_delete_objects',
            ),
        ),
        migrations.AddField(
            model_name='s3exportstorage',
            name='can_delete_objects',
            field=models.BooleanField(
                blank=True,
                help_text='Deletion from storage enabled',
                null=True,
                verbose_name='can_delete_objects',
            ),
        ),
    ]
