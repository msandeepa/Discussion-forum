# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151130_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(max_length=15, choices=[(b'Datastructure', b'Datastructure'), (b'WebProgramming', b'WebProgramming'), (b'General', b'General'), (b'Java', b'Java'), (b'DBMS', b'DBMS')]),
        ),
    ]
