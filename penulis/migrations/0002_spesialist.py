# Generated by Django 4.0.3 on 2022-05-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penulis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spesialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_spesialist', models.CharField(blank=True, max_length=100, null=True)),
                ('spesialist', models.CharField(blank=True, max_length=50, null=True)),
                ('tentang', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
