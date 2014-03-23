# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_news_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='header_image',
            field=models.ForeignKey(to='content.Image', to_field='id', default=0),
            preserve_default=False,
        ),
    ]
