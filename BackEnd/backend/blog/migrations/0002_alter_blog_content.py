# Generated by Django 4.2 on 2023-06-06 21:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
