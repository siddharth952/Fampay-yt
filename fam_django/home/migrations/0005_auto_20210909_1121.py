# Generated by Django 3.2.7 on 2021-09-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_video_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail_url',
            field=models.CharField(default='1999-02-20', max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]