# Generated by Django 4.2.7 on 2023-11-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_course_prerequisites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_type',
        ),
    ]
