# Generated by Django 2.1.4 on 2018-12-24 18:33

from django.db import migrations, models
import kernel.utils.upload_to


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=127)),
                ('url', models.URLField(verbose_name='URL')),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, max_length=255, null=True, upload_to=kernel.utils.upload_to.UploadTo('links', 'logos'))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]