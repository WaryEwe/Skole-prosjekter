# Generated by Django 5.1.4 on 2025-01-09 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowingmodel',
            old_name='borrower_id',
            new_name='borrowing_id',
        ),
    ]