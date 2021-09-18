# Generated by Django 3.2.6 on 2021-09-17 23:29

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, default='defaults/cover.png', null=True, upload_to='covers/')),
                ('isbn', models.CharField(blank=True, max_length=255, null=True)),
                ('rate', models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('goodreads_rate', models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='books', to='core.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, default='defaults/avatar.png', upload_to='avatars/')),
                ('social_media_username', models.CharField(blank=True, choices=[('twitter', 'Twitter')], max_length=255)),
                ('social_media_link', models.URLField(blank=True)),
                ('is_invited', models.BooleanField(default=False)),
                ('favorite_books', models.ManyToManyField(blank=True, related_name='favorite_books', to='core.Book')),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('read_later_books', models.ManyToManyField(blank=True, related_name='read_later_books', to='core.Book')),
                ('readed_books', models.ManyToManyField(blank=True, related_name='readed_books', to='core.Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='CYA3KZ', max_length=255, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConfirmCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='560272', max_length=255, unique=True)),
                ('expires', models.DateTimeField(default=datetime.datetime(2021, 9, 17, 23, 39, 37, 392853, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='core.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='translators',
            field=models.ManyToManyField(blank=True, related_name='books', to='core.Translator'),
        ),
    ]
