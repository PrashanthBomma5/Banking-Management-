# Generated by Django 3.2.23 on 2024-04-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0008_transactions_account_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='source_account',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
