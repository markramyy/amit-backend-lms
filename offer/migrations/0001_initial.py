# Generated by Django 4.2.7 on 2023-11-16 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('max_capacity', models.PositiveIntegerField()),
                ('current_enrollment', models.PositiveIntegerField(default=0)),
                ('waiting_list_status', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.BooleanField(default=False)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_offer', to='course.course')),
            ],
        ),
    ]
