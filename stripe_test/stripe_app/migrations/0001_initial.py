# Generated by Django 5.0.2 on 2024-02-29 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('price', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'description', 'price')},
            },
        ),
    ]
