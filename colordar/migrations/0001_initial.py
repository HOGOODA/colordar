# Generated by Django 3.1.7 on 2021-02-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='최대 50자 내로 입력가능합니다.', max_length=50, verbose_name='제목')),
                ('description', models.TextField(default='', verbose_name='내용')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='내용')),
            ],
        ),
    ]
