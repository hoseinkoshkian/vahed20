# Generated by Django 5.1.4 on 2025-01-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='last_name',
        ),
    ]
