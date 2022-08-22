# Generated by Django 4.1 on 2022-08-22 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_customuser_is_verified_usertype_is_default_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.usertype', default=1),
        ),
    ]