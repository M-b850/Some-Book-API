# Generated by Django 3.2.6 on 2022-04-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20220419_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='source_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
