# Generated by Django 5.0 on 2024-01-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_bankruptmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankruptModel',
        ),
        migrations.AddField(
            model_name='transaction',
            name='is_bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]
