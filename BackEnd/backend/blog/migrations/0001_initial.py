# Generated by Django 4.2 on 2023-05-30 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=150)),
                ("author", models.CharField(max_length=40)),
                ("content", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("category", models.CharField(max_length=40)),
                ("image", models.ImageField(upload_to="blog/")),
                ("slug", models.SlugField()),
            ],
        ),
    ]