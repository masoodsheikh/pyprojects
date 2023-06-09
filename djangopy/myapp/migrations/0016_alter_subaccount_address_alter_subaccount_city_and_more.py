# Generated by Django 4.2.1 on 2023-06-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_sub_account_subaccount_main_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaccount',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='customer_website',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='phone1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='phone2',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='sub_account_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
