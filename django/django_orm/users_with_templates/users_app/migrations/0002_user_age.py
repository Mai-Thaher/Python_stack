# Generated by Django 2.2.4 on 2024-03-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]