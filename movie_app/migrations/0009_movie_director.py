# Generated by Django 4.0.3 on 2022-03-26 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_director_remove_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movie_app.director'),
        ),
    ]
