# Generated by Django 3.0.4 on 2020-04-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BYARENT', '0002_home_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]