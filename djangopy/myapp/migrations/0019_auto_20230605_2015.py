# Generated by Django 4.2.1 on 2023-06-05 15:15
from django.db import migrations, models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_subaccount_main_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaccount',
            name='opening_balance',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]