# Generated by Django 2.2.4 on 2024-04-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
