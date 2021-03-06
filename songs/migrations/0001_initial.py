# Generated by Django 4.0.6 on 2022-07-14 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of the song', max_length=100)),
                ('genre', models.CharField(choices=[('reggaeton', 'Reggaeton'), ('bachata', 'Bachata'), ('rock', 'Rock'), ('indie', 'Indie'), ('banda', 'Banda'), ('hiphop', 'Hip hop'), ('balada', 'Balada')], help_text='The genre of the song', max_length=50)),
                ('author', models.CharField(help_text='The author and featurings of the song', max_length=100)),
                ('lyrics', models.TextField(blank=True, help_text='The original lyrics of the song', null=True)),
            ],
        ),
    ]
