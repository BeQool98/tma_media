# Generated by Django 4.2 on 2024-10-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmasite', '0009_missionandvision_vision_body_alter_brochure_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
