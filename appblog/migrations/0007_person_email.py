# Generated by Django 4.2.7 on 2024-05-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0006_message_created_message_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
