# Generated by Django 4.2.7 on 2023-11-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_remove_content_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.PositiveIntegerField(default=8),
        ),
    ]
