# Generated by Django 2.1.7 on 2019-09-03 14:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('userId', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('workId', models.IntegerField()),
                ('department', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('tellPhone', models.CharField(max_length=11)),
            ],
        ),
    ]
