# Generated by Django 2.1.7 on 2019-03-18 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_theme', models.CharField(max_length=200)),
                ('activity_creator', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_name', models.CharField(max_length=200)),
                ('sign_date', models.DateTimeField(verbose_name='date sign')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acsign.Activity')),
            ],
        ),
    ]
