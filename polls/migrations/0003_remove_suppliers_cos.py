# Generated by Django 4.2.3 on 2023-07-29 17:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_suppliers_cos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="suppliers",
            name="cos",
        ),
    ]