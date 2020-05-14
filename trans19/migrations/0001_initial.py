# Generated by Django 3.0.5 on 2020-05-14 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('district', models.CharField(choices=[('Hong Kong Island', (('Central and Western', 'Central and Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai'))), ('Kowloon', (('Sham Shui Po', 'Sham Shui Po'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'))), ('New Teritories', (('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long')))], max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('x_coord', models.IntegerField()),
                ('y_coord', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_id', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('date_case_confirmed', models.DateField()),
                ('case_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('detail', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans19.Location')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans19.Patient')),
            ],
        ),
    ]
