# Generated by Django 5.0.7 on 2024-12-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngos', '0004_alter_ngo_completed_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='completed_project',
            field=models.CharField(default='No Completed Projects', max_length=255),
        ),
    ]
