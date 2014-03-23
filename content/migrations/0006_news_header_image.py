# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='header_image',
            field=models.ForeignKey(to_field='id', to='content.Image', default=0),
            preserve_default=False,
        ),
    ]
