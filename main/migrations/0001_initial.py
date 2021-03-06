# Generated by Django 3.1.1 on 2020-09-10 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Введіть назву категорії')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_page', models.CharField(default='BudModa', max_length=50, verbose_name='Title (seo) сторінки')),
                ('title_m', models.CharField(max_length=100, verbose_name='Назва сторінки')),
                ('slide_on_index', models.ImageField(blank=True, null=True, upload_to='static/media', verbose_name='Картинка на головній сторінці')),
                ('background_img', models.ImageField(blank=True, null=True, upload_to='static/media', verbose_name='Беграундна картинка')),
                ('slide_img_one', models.ImageField(blank=True, null=True, upload_to='static/media', verbose_name='1 Картинка в слайдері')),
                ('slide_img_two', models.ImageField(blank=True, null=True, upload_to='static/media', verbose_name='2 Картинка в слайдері')),
                ('slide_img_three', models.ImageField(blank=True, null=True, upload_to='static/media', verbose_name='3 Картинка в слайдері')),
                ('title_text', models.CharField(max_length=200, verbose_name='Заголовок тексту')),
                ('main_text', models.TextField(verbose_name='Опис сторінки')),
                ('url_page', models.SlugField(default=0, max_length=130, unique=True, verbose_name='Юрл сторінки')),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.typepage')),
            ],
            options={
                'verbose_name': 'Сторінка',
                'verbose_name_plural': 'Сторінки',
            },
        ),
    ]
