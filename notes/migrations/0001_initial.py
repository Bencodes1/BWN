# Generated by Django 3.2 on 2021-04-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='untitled', max_length=160)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
    ]
