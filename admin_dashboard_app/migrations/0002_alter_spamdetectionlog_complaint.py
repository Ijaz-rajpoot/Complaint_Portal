# Generated by Django 5.2 on 2025-05-06 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard_app', '0001_initial'),
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spamdetectionlog',
            name='complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_spam_logs', to='student_app.complaint'),
        ),
    ]
