# Generated by Django 5.0 on 2023-12-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Project',
        ),
    ]
