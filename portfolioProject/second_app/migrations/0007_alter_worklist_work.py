# Generated by Django 3.2.9 on 2022-01-02 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0006_auto_20220102_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklist',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='w_list', to='second_app.ourwork'),
        ),
    ]
