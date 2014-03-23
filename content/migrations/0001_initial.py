# encoding: utf8
from django.db import models, migrations
import goatnails.db.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', goatnails.db.models.ImageWithThumbsField(upload_to='images')),
                ('credit', models.CharField(max_length=50)),
                ('caption', models.CharField(blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
