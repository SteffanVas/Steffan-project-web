# Generated by Django 4.2.4 on 2023-08-05 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_tipmodel_title'),
        ('recipes', '0013_alter_comment_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.datacontrib'),
        ),
    ]
