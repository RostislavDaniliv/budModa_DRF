from django.db import models
from django.urls import reverse


class TypePage(models.Model):
    name = models.CharField('Введіть назву категорії', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Page(models.Model):
    title_page = models.CharField('Title (seo) сторінки', default='BudModa', max_length=50)
    title_m = models.CharField('Назва сторінки', max_length=100)
    slide_on_index = models.ImageField('Картинка на головній сторінці', upload_to='static/media', null=True, blank=True)
    background_img = models.ImageField('Беграундна картинка', upload_to='static/media', null=True, blank=True)
    slide_img_one = models.ImageField('1 Картинка в слайдері', upload_to='static/media', null=True, blank=True)
    slide_img_two = models.ImageField('2 Картинка в слайдері', upload_to='static/media', null=True, blank=True)
    slide_img_three = models.ImageField('3 Картинка в слайдері', upload_to='static/media', null=True, blank=True)
    title_text = models.CharField('Заголовок тексту', max_length=200)
    main_text = models.TextField('Опис сторінки')
    categories = models.ForeignKey('TypePage', on_delete=models.SET_NULL, null=True)
    url_page = models.SlugField('Юрл сторінки', max_length=130, default=0, unique=True)

    def display_typepage(self):
        return ', '.join([categories.name for categories in self.categories.all()[:3]])
        display_typepage.short_description = 'TypePage'

    def __str__(self):
        return self.title_m

    def get_absolute_url(self):
        return reverse('page_d', kwargs={"slug": self.url_page})

    class Meta:
        verbose_name = 'Сторінка'
        verbose_name_plural = 'Сторінки'