# Generated by Django 4.2.1 on 2023-05-26 18:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusName', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campusID', models.IntegerField(blank=True, default='')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
