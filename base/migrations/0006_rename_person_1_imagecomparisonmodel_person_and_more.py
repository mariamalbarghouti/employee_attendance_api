# Generated by Django 5.0.6 on 2024-06-21 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_imagecomparisonmodel_rename_image_imagemodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imagecomparisonmodel",
            old_name="person_1",
            new_name="person",
        ),
        migrations.RemoveField(
            model_name="imagecomparisonmodel",
            name="person_2",
        ),
        migrations.RemoveField(
            model_name="imagemodel",
            name="name",
        ),
    ]