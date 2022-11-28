# Generated by Django 3.2.16 on 2022-11-27 02:15

import NEMO.utilities
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0042_version_4_3_0'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the discipline', max_length=200, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name']
            },
        ),
        migrations.CreateModel(
            name='SafetyTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the training', max_length=200, unique=True)),
                ('display_order', models.IntegerField(help_text="Safety trainings are sorted according to display order. The lowest value category is displayed first in the 'Users' page.")),
            ],
            options={
                'abstract': False,
                'ordering': ['display_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='OnboardingPhase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the onboarding phase', max_length=200, unique=True)),
                ('display_order', models.IntegerField(help_text="Onboarding phases are sorted according to display order. The lowest value category is displayed first in the 'Users' page.")),
            ],
            options={
                'abstract': False,
                'ordering': ['display_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to=NEMO.utilities.get_project_document_filename, verbose_name='Document')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('name', models.CharField(blank=True, help_text='The optional name to display for this document', max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(related_name="project_documents", on_delete=django.db.models.deletion.CASCADE, to='NEMO.project')),
            ],
            options={
                'verbose_name_plural': 'Project documents',
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NEMO.discipline'),
        ),
        migrations.CreateModel(
            name='UserDocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to=NEMO.utilities.get_user_document_filename, verbose_name='Document')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('name', models.CharField(blank=True, help_text='The optional name to display for this document', max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name="user_documents", on_delete=django.db.models.deletion.CASCADE, to='NEMO.user')),
            ],
            options={
                'verbose_name_plural': 'User documents',
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NEMO.discipline'),
        ),
        migrations.AddField(
            model_name='user',
            name='onboarding_phases',
            field=models.ManyToManyField(blank=True, to='NEMO.OnboardingPhase'),
        ),
        migrations.AddField(
            model_name='user',
            name='safety_trainings',
            field=models.ManyToManyField(blank=True, to='NEMO.SafetyTraining'),
        ),
    ]
