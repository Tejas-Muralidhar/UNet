# Generated by Django 5.1.2 on 2024-12-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngos', '0005_alter_ngo_completed_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='account_number',
            field=models.CharField(default='0000000000000000', max_length=16),
        ),
    ]
