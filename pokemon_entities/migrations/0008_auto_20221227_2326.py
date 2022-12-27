# Generated by Django 3.1.14 on 2022-12-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='default title_en', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='default title_jp', max_length=200),
            preserve_default=False,
        ),
    ]