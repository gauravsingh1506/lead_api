# Generated by Django 2.1 on 2020-11-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location_type', models.CharField(choices=[['Country', 'Country'], ['City', 'City'], ['Zip', 'Zip']], max_length=10)),
                ('location_string', models.TextField()),
                ('status', models.CharField(choices=[['Created', 'Created'], ['Contacted', 'Contacted']], max_length=10)),
                ('communication', models.TextField(null=True)),
            ],
        ),
    ]
