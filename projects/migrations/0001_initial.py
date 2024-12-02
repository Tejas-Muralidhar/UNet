# Generated by Django 5.1.2 on 2024-10-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('ongoing', 'Ongoing'), ('future_event', 'Future Event'), ('cancelled', 'Cancelled')], max_length=20)),
            ],
        ),
    ]