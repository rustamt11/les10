# Generated by Django 4.2.2 on 2023-06-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('status', models.CharField(choices=[('st', 'Учусь'), ('wk', 'Работаю'), ('sd', 'Туплю'), ('mm', 'Мамкин миллиардер'), ('mp', 'Мамин бродяга, папин симпотяга')], max_length=50)),
                ('salary', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]