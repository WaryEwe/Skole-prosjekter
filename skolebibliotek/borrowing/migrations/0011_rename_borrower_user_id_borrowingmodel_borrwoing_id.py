# Generated by Django 5.1.4 on 2025-01-13 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0010_alter_borrowingmodel_borrower_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowingmodel',
            old_name='borrower_user_id',
            new_name='borrwoing_id',
        ),
    ]