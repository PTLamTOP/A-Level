# Generated by Django 3.0.2 on 2020-01-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200120_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='token',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
