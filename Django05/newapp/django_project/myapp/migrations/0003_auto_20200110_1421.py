# Generated by Django 2.2 on 2020-01-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200110_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='sex',
            field=models.IntegerField(choices=[(1, 'male'), (2, 'female')], null=True),
        ),
    ]
