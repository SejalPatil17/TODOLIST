# Generated by Django 5.0 on 2023-12-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("taskTitle", models.CharField(max_length=30)),
                ("taskDesc", models.CharField(max_length=30)),
                ("time", models.DateTimeField(auto_now_add=True)),
               
  
            ],
        ),
    ]