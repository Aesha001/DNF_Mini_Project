# Generated by Django 4.2.6 on 2023-11-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MailBox",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("email_id", models.EmailField(max_length=150)),
                ("subject", models.CharField(max_length=150)),
                ("message", models.TextField()),
            ],
        ),
    ]