# Generated by Django 4.2 on 2023-05-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_favoritepost_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_checked',
            field=models.BooleanField(default=False, verbose_name='Ручная проверка'),
        ),
    ]
