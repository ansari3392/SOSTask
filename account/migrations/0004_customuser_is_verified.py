# Generated by Django 4.1 on 2022-08-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_managers_remove_customuser_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
