# Generated by Django 4.2.1 on 2023-06-05 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_subaccount_main_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaccount',
            name='main_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_account', to='myapp.main_account'),
        ),
    ]