# Generated by Django 3.2.7 on 2021-10-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_requestresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestresult',
            name='status_code',
            field=models.CharField(default='0', max_length=10, verbose_name='Статус ответа'),
        ),
    ]