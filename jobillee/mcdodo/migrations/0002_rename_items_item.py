# Generated by Django 5.0.2 on 2024-03-18 16:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mcdodo", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="items",
            new_name="item",
        ),
    ]
