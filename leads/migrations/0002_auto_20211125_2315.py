# Generated by Django 3.2.9 on 2021-11-25 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Leads', 'Lead')
    ]