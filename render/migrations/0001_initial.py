# Generated by Django 3.2.16 on 2022-10-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('image_onmouseover', models.ImageField(default='portfolio/images/', upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]