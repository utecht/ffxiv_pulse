# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import goatnails.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('avatar', goatnails.db.models.ImageWithThumbsField(blank=True, upload_to='images')),
                ('real_pic', goatnails.db.models.ImageWithThumbsField(blank=True, upload_to='images')),
                ('bio', models.TextField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
