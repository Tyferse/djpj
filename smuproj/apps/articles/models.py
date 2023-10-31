import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    article_title = models.CharField('название статьи',
                                     max_length=250)
    article_text = models.TextField('текст статьи')
    pub = models.DateTimeField('дата публикации')
    
    def __str__(self):
        return self.article_title
    
    def was_published_recently(self):
        return self.pub >= (timezone.now() - datetime.timedelta(days=7))
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора',
                                   max_length=75)
    comment_text = models.CharField('текст комментария',
                                    max_length=500)
    
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    