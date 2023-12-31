# Generated by Django 4.2.2 on 2023-11-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('addr', models.CharField(max_length=250)),
                ('dob', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('purpose', models.CharField(max_length=250)),
                ('material', models.CharField(max_length=250)),
            ],
        ),
    ]
