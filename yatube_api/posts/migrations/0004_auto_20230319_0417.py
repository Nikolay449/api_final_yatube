# Generated by Django 3.2.16 on 2023-03-19 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230319_0328'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_not_following',
        ),
    ]
