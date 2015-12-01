# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_question_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
    ]
