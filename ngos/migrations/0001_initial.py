# Generated by Django 5.1.2 on 2024-10-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('web_links', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='ngo_profile_pictures/')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
