# Generated by Django 3.0.5 on 2021-06-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greek_food', '0006_delete_tablelistview'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
    ]
