# Generated by Django 4.2 on 2024-10-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmasite', '0004_aboutus_brands_callback_headerinfo_messages_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='top_header',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='headerinfo',
            name='top_small',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='whychooseus',
            name='tab_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
