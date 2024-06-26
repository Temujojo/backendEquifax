# Generated by Django 5.0.6 on 2024-05-20 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('certificate', models.CharField(max_length=100)),
                ('init_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CandidateJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('init_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=300)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidateeducation')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidatejobs')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.language')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.level'),
        ),
    ]
