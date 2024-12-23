# Generated by Django 5.1.4 on 2024-12-20 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0002_faculty_slug_group_slug'),
        ('timetable', '0006_alter_schedule_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('pair_number', 'group', 'date')},
        ),
    ]
