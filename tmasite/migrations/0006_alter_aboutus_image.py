# Generated by Django 4.2 on 2024-10-18 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmasite', '0005_alter_aboutus_top_header_alter_headerinfo_top_small_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, default='media/author_img_default.png', null=True, upload_to='media'),
        ),
    ]