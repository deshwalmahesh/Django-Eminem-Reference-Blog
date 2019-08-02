# Generated by Django 2.1.1 on 2019-08-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190801_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='is_approved',
            new_name='edit',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_published',
        ),
        migrations.AddField(
            model_name='comment',
            name='edited_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
