# Generated by Django 4.1 on 2022-09-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Пуста назва', max_length=50, verbose_name='Назва')),
                ('anons', models.CharField(default='Пустий анонс', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Текст новини')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
    ]
