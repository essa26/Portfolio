# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150920_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'skill'),
        ),
    ]
