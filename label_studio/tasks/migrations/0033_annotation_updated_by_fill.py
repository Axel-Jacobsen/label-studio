# Generated by Django 3.2.16 on 2022-11-18 23:38

from core.models import AsyncMigrationStatus
from core.redis import start_job_async_or_sync
from django.conf import settings
from django.db import migrations, models
from django.db.models import F

from projects.models import Project
from tasks.models import Annotation

import logging


def _fill_annotations_updated_by():
    projects = Project.objects.all()
    for project in projects.iterator():
        migration = AsyncMigrationStatus.objects.filter(
            project=project, name='0033_annotation_updated_by_fill'
        ).first()
        if migration and migration.status == AsyncMigrationStatus.STATUS_FINISHED:
            # Migration for this project already done
            continue

        migration = AsyncMigrationStatus.objects.create(
            project=project,
            name='0033_annotation_updated_by_fill',
            status=AsyncMigrationStatus.STATUS_STARTED,
        )

        Annotation.objects.filter(project=project).update(updated_by=F('completed_by'))
        migration.status = AsyncMigrationStatus.STATUS_FINISHED
        migration.save()


def forward(apps, _):
    annotations = Annotation.objects.all()

    if settings.VERSION_EDITION == 'Community':
        if annotations.count() > 100000:
            command = 'label-studio annotations_fill_updated_by'
            logger = logging.getLogger(__name__)
            logger.error(
                "There are over 100,000 annotations in this label studio instance, please run this "
                f"migration manually using {command}"
            )
            return

    start_job_async_or_sync(_fill_annotations_updated_by)


def backward(apps, _):
    pass


class Migration(migrations.Migration):
    dependencies = [('tasks', '0032_annotation_updated_by')]

    operations = [migrations.RunPython(forward, backward)]
