# Generated by Django 3.1.1 on 2020-12-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('food', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]