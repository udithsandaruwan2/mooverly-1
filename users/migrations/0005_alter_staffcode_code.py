# Generated by Django 5.0.4 on 2024-05-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_staffcode_profile_staff_code_staffcode_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffcode',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]