# Generated by Django 5.0.1 on 2024-01-15 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_identifier', models.CharField(blank=True, max_length=20, null=True)),
                ('class_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_info', to='webapp.student')),
            ],
        ),
    ]
