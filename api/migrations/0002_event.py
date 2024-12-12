# Generated by Django 5.1.3 on 2024-12-12 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=32)),
                ('team2', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
                ('score1', models.IntegerField(blank=True, null=True)),
                ('score2', models.IntegerField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.group')),
            ],
        ),
    ]
