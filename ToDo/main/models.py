from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    content = models.TextField(verbose_name='Содержание', max_length=1024)
    time = models.DateField('Дата создания')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
