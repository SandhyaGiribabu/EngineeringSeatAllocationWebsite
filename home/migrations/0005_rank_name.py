# Generated by Django 5.0.6 on 2024-05-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_rank_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]