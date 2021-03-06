# Generated by Django 2.2 on 2020-01-24 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_is_returned'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='returned_item', to='orders.OrderItem')),
            ],
        ),
    ]
