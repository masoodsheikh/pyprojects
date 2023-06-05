# Generated by Django 4.2.1 on 2023-06-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_subaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledger', to='myapp.subaccount'),
        ),
    ]