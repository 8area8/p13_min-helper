# Generated by Django 4.0.1 on 2022-01-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0010_alter_anime_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='cover_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='english_name',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodes_count',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='japanese_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='score',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
