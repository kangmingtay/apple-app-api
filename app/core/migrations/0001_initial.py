# Generated by Django 2.1.14 on 2019-11-24 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('num_outlets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=60)),
                ('pdus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Pdu')),
            ],
        ),
    ]
