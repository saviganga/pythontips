# Generated by Django 3.2 on 2021-06-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0005_alter_tweet_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tip',
            field=models.TextField(),
        ),
    ]
