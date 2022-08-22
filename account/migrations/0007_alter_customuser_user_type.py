# Generated by Django 4.1 on 2022-08-22 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.usertype'),
        ),
    ]