# Generated by Django 2.2.7 on 2019-11-09 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='qwerty', max_length=255),
        ),
    ]
