from django.db import models


class Articles(models.Model):
    objects = None
    title = models.CharField('ФИО', max_length=100)
    role = models.CharField('Должность', max_length=50)
    skills = models.CharField('Навыки', max_length=250)
    full_text = models.TextField('Основной текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/new/{self.id}'

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
