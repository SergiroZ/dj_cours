# Generated by Django 2.1.3 on 2018-11-06 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pic', models.ImageField(blank=True, default='place_icons/default.png', upload_to='place_icons/', verbose_name='Аватарка ')),
                ('home_country', models.CharField(choices=[('Беларусь', 'Беларусь'), ('Россия', 'Россия'), ('Украина', 'Украина')], db_index=True, default=('Беларусь', 'Беларусь'), max_length=1000, verbose_name='Страна')),
                ('home_city', models.CharField(db_index=True, default='Минск', max_length=1000, verbose_name='Город')),
                ('home_street', models.CharField(db_index=True, default='пр.Рокоссовского', max_length=1000, verbose_name='Улица')),
                ('home_building', models.CharField(db_index=True, default=1, max_length=1000, verbose_name='Дом')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
