# Generated by Django 3.0.2 on 2020-01-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
    ]