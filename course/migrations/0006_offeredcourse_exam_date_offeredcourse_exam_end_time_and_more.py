# Generated by Django 5.1.4 on 2025-01-14 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_offeredcourse_class_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='offeredcourse',
            name='exam_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='offeredcourse',
            name='exam_end_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='offeredcourse',
            name='exam_start_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offeredcourse',
            name='class_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.class', verbose_name='کد کلاس ارائه شده'),
        ),
    ]
