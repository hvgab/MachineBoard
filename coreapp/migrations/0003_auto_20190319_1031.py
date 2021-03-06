# Generated by Django 2.1.7 on 2019-03-19 09:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_auto_20190319_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2019, 3, 19, 9, 31, 12, 654460, tzinfo=utc))),
                ('salecount', models.IntegerField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.Agent')),
            ],
        ),
        migrations.RemoveField(
            model_name='sale',
            name='agent',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
