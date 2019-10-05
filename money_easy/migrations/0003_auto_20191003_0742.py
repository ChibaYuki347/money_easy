# Generated by Django 2.2.1 on 2019-10-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_easy', '0002_payitem_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payitem',
            old_name='deadline',
            new_name='duedate',
        ),
        migrations.AddField(
            model_name='payitem',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('info', 'normal'), ('success', 'low')], default='normal', max_length=50),
        ),
    ]