# Generated by Django 4.2.1 on 2023-06-04 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_main_account_sub_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sub_account',
        ),
    ]
