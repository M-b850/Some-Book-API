# Generated by Django 3.2.6 on 2021-10-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='social_media_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
