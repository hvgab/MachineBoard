# Generated by Django 2.1.7 on 2019-03-19 09:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonthTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('target', models.IntegerField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2019, 3, 19, 9, 28, 8, 256032, tzinfo=utc))),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='WeekTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('target', models.IntegerField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.Agent')),
            ],
        ),
    ]
