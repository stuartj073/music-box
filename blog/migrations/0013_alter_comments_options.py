# Generated by Django 3.2 on 2022-02-24 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_comments_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date']},
        ),
    ]
