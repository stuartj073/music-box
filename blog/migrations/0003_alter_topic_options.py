# Generated by Django 3.2 on 2022-01-10 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220110_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name_plural': 'Topics'},
        ),
    ]
