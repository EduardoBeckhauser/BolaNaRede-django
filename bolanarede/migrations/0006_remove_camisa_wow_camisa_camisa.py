# Generated by Django 4.2.5 on 2023-09-18 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('bolanarede', '0005_camisa_wow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camisa',
            name='wow',
        ),
        migrations.AddField(
            model_name='camisa',
            name='camisa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
