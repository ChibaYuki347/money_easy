# Generated by Django 2.2.1 on 2019-09-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_easy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payitem',
            name='title',
            field=models.CharField(default='title', max_length=30, verbose_name='タイトル'),
        ),
    ]