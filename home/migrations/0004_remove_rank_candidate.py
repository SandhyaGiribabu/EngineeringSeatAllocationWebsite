# Generated by Django 5.0.6 on 2024-05-14 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_candidate_aadhar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='candidate',
        ),
    ]
