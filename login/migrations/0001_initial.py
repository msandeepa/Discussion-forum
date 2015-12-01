# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=15)),
                ('question', models.CharField(max_length=300)),
                ('likes', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
    ]
