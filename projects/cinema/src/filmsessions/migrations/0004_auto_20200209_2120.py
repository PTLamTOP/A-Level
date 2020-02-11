# Generated by Django 2.2 on 2020-02-09 18:20

from django.db import migrations
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filmsessions', '0003_auto_20200209_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='picture',
            field=django_fields.fields.DefaultStaticImageField(blank=True, height_field=500, upload_to='pictures/%Y/%m/%d', width_field=500),
        ),
    ]
