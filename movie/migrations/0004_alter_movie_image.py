# Generated by Django 5.0.1 on 2024-02-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movie'),
        ),
    ]
