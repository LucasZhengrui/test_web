# Generated by Django 4.2.1 on 2023-05-31 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='User_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
