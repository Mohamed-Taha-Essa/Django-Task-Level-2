# Generated by Django 4.2 on 2024-02-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='hellow', max_length=100),
            preserve_default=False,
        ),
    ]
