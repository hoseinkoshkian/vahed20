# Generated by Django 5.1.4 on 2025-01-14 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_offeredcourse_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredcourse',
            name='class_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.class', verbose_name='استاد'),
        ),
    ]
