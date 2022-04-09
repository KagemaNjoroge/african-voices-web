# Generated by Django 4.0.2 on 2022-04-08 20:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('lang_id', models.CharField(max_length=100)),
                ('lang_code', models.CharField(max_length=100)),
                ('lang_name', models.CharField(max_length=100)),
                ('pass0_utt', models.CharField(max_length=100)),
                ('pass0_mcd', models.CharField(max_length=100)),
                ('pass1_utt', models.CharField(max_length=100)),
                ('pass1_mcd', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('rfs_utt', models.CharField(max_length=100)),
                ('base', models.CharField(max_length=100)),
                ('rfs', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]