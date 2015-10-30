# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('pic', models.FileField(null=True, upload_to=main.models.generate_filename, blank=True)),
            ],
        ),
    ]
