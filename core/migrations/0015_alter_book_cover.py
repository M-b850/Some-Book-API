# Generated by Django 3.2.6 on 2021-12-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20211124_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='covers/default.png', null=True, upload_to='covers/'),
        ),
    ]
