# Generated by Django 2.2.4 on 2024-03-31 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='no available notes'),
            preserve_default=False,
        ),
    ]
