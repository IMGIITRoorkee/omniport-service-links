# Generated by Django 2.2.6 on 2020-01-11 19:30

from django.db import migrations, models
import formula_one.utils.upload_to
import formula_one.validators.aspect_ratio


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='logo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=formula_one.utils.upload_to.UploadTo('links', 'logos'), validators=[formula_one.validators.aspect_ratio.AspectRatioValidator(1, 0.1)]),
        ),
    ]
