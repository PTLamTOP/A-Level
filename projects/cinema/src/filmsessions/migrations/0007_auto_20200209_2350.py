# Generated by Django 2.2 on 2020-02-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmsessions', '0006_auto_20200209_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
