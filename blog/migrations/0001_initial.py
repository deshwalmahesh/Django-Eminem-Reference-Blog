# Generated by Django 2.2.2 on 2019-06-19 19:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(default=datetime.datetime(2019, 6, 19, 19, 55, 16, 212818, tzinfo=utc))),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('published_date', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(max_length=25, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=1024)),
                ('created_date', models.DateField(default=datetime.datetime(2019, 6, 19, 19, 55, 16, 214818, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='blog.Post')),
            ],
        ),
    ]
