# Generated by Django 3.2 on 2022-01-10 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.topic'),
        ),
    ]
