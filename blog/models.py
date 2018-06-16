from django.db import models
from mdeditor.fields import MDTextField
from django.urls import reverse
from users.models import User
from core.models import BaseModel


class Base(BaseModel):
    name = models.CharField('名字', max_length=50)


class Tags(models.Model):
    '''Tags
    ---
    '''
    name = models.CharField('标签名', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    '''分类
    ---
    '''
    name = models.CharField('标签名', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Article(models.Model):
    '''文章模型类'''

    STATUS_CHOICES = (
        ('d', 'part'),
        ('p', 'Published'),
    )  # 文章状态

    title = models.CharField('文章标题', max_length=200)
    body = MDTextField()
    created_date = models.DateTimeField('发布日期', auto_now_add=True)
    modified_date = models.DateTimeField('更新日期', auto_now=True)
    status = models.CharField(
        '文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    abstract = models.CharField(
        '摘要',
        max_length=54,
        blank=True,
        null=True,
        help_text='可选项，若为空则摘取正文前54个字符。')
    thumbnail = models.ImageField(
        upload_to='article/thumbnail',
        blank=True,
        null=True,
        verbose_name='缩略图')
    # 阅读量
    views = models.PositiveIntegerField('浏览量', default=0)
    # 是否置顶
    topped = models.BooleanField('置顶', default=False)
    tag = models.ManyToManyField(
        Tags, blank=True, verbose_name='标签', default='')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='分类',
        default='')
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})
