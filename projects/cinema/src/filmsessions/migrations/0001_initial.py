# Generated by Django 2.2 on 2020-02-12 18:49

from django.db import migrations, models
import django.db.models.deletion
import django_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('picture', django_fields.fields.DefaultStaticImageField(blank=True, upload_to='pictures/%Y/%m/%d')),
                ('genre', models.CharField(choices=[('AC', 'Action'), ('AD', 'Adventure'), ('CM', 'Comedy'), ('CR', 'Crime'), ('DR', 'Drama'), ('HS', 'Historical'), ('HR', 'Horror'), ('MC', 'Musicals'), ('SC', 'Science'), ('WR', 'War'), ('WN', 'Westerns')], max_length=2)),
                ('description', models.TextField()),
                ('release_year', models.DateField()),
                ('period_from', models.DateField()),
                ('period_to', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilmSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_from', models.DateTimeField()),
                ('time_to', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('available_seats', models.PositiveIntegerField(blank=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='filmsessions.Film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='halls.Hall')),
            ],
        ),
    ]
