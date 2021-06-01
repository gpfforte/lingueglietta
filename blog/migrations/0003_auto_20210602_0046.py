# Generated by Django 3.2 on 2021-06-01 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-published_date',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='status',
            new_name='published',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
