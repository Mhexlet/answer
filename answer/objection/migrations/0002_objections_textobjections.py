# Generated by Django 4.2.2 on 2023-06-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objections',
            name='textObjections',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
