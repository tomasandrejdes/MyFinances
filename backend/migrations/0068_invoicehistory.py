# Generated by Django 5.1.1 on 2024-10-30 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0067_remove_apiauthtoken_expired_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvoiceHistory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("version", models.IntegerField()),
                ("changes", models.JSONField()),
                ("invoice", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="history", to="backend.invoice")),
            ],
        ),
    ]
