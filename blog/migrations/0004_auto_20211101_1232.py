# Generated by Django 3.2 on 2021-11-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210602_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]