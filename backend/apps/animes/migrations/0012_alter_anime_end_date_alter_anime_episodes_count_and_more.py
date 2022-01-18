# Generated by Django 4.0.1 on 2022-01-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0011_alter_anime_cover_image_alter_anime_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='end_date',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodes_count',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='score',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='start_date',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
