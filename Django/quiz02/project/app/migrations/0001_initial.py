# Generated by Django 2.0.7 on 2020-06-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.BooleanField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
