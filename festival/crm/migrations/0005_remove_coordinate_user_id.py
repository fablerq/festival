# Generated by Django 2.2.7 on 2019-11-10 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_coordinate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinate',
            name='user_id',
        ),
    ]
