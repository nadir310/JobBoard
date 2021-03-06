# Generated by Django 3.0.8 on 2020-07-24 14:35

from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('cpver_letter', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Part time', 'Part time'), ('Full time', 'Full time')], max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('published_at', models.TimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('salery', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to=job.models.image_upload)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category')),
            ],
        ),
    ]
