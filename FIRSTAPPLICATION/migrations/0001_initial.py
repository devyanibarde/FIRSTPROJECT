# Generated by Django 4.1.5 on 2023-02-02 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("phone_no", models.CharField(max_length=100)),
                ("email_id", models.CharField(max_length=200)),
                (
                    "pid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="FIRSTAPPLICATION.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("city", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                (
                    "pid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="FIRSTAPPLICATION.person",
                    ),
                ),
            ],
        ),
    ]
