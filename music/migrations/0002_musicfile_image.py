# Generated by Django 4.2.2 on 2023-06-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicfile',
            name='image',
            field=models.ImageField(default='', max_length=10000, null=True, upload_to=''),
        ),
    ]
