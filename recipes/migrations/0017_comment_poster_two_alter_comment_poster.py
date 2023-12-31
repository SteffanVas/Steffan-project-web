# Generated by Django 4.2.4 on 2023-08-06 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_tipmodel_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0016_alter_comment_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='poster_two',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, to='web.datacontrib'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
