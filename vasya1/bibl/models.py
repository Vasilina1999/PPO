from django.db import models

class Bibld(models.Model):
    title_bib = models.CharField('Название', max_length=50)
    anons_bib = models.CharField('Анонс', max_length=250)
    full_text_bib = models.TextField('Описание')
    date_bib = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title_bib

    def get_absolute_url(self):
     return f'/bibl/{self.id}'
