# Generated by Django 4.1 on 2022-08-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_delete_videoproxy_videopublishedproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
