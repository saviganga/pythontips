# Generated by Django 3.2 on 2021-06-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_alter_tweet_tip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tip',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
