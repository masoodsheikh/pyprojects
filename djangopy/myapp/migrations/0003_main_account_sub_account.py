# Generated by Django 4.2.1 on 2023-06-04 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_acount_name', models.CharField(max_length=100)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='myapp.account_type')),
            ],
        ),
        migrations.CreateModel(
            name='sub_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_account_name', models.CharField(max_length=100)),
                ('main_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='myapp.main_account')),
            ],
        ),
    ]
