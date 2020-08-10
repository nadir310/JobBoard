# Generated by Django 3.0.8 on 2020-08-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=50, null=1, verbose_name='student age')),
                ('name', models.IntegerField(max_length=50, null=1, verbose_name='student name')),
                ('phone', models.CharField(max_length=50, null=1, verbose_name='student phone')),
            ],
        ),
    ]