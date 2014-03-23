# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_editor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField()),
                ('author', models.ForeignKey(to='content.Editor', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
