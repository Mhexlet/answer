# Generated by Django 4.2.2 on 2023-06-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objection', '0002_objections_textobjections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objections',
            name='textObjections',
            field=models.TextField(max_length=1000),
        ),
    ]
