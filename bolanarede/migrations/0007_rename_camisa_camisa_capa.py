# Generated by Django 4.2.5 on 2023-09-18 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolanarede', '0006_remove_camisa_wow_camisa_camisa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camisa',
            old_name='camisa',
            new_name='capa',
        ),
    ]
