# Generated by Django 4.0.5 on 2022-06-09 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_article_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='article_date',
            new_name='date',
        ),
    ]
