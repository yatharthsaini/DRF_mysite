# Generated by Django 4.2.6 on 2023-11-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_moviedata_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviedata",
            name="image",
            field=models.ImageField(
                default="Images/None/Noimg.jpg", upload_to="Images/"
            ),
        ),
    ]