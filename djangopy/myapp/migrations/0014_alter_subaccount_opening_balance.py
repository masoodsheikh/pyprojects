# Generated by Django 4.2.1 on 2023-06-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_voucherdetail_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaccount',
            name='opening_balance',
            field=models.IntegerField(),
        ),
    ]
