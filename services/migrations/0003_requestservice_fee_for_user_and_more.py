# Generated by Django 4.1 on 2022-08-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_requestservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestservice',
            name='fee_for_user',
            field=models.PositiveIntegerField(blank=True, help_text='این فیلد در لحظه ی تایید شدن درخواست، به صورت اتوماتیک ذخیره میشود تا در صورت تغییر درصد کارمزد، درخواست های ثبت شده تغییر قیمت نداشته باشند.', null=True),
        ),
        migrations.AlterField(
            model_name='requestservice',
            name='service_price',
            field=models.PositiveBigIntegerField(blank=True, help_text='این فیلد در لحظه ی تایید شدن درخواست، به صورت اتوماتیک ذخیره میشود تا در صورت تغییر قیمت سرویس، درخواست های ثبت شده تغییر قیمت نداشته باشند.', null=True),
        ),
    ]
