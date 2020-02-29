from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, default='社会')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, default='热点')

    def __str__(self):
        return self.name


class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式，避免两个关联表的数据不一致。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)

    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created_time = models.DateTimeField(default=timezone.now)

    total_views = models.PositiveIntegerField(default=0)

    # 分类用外键，即一篇文章只能对应分类，但一个分类下可以有多篇文章
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # 标签采用多对多，即一篇文章可以有多个标签，一个标签下也有多篇文章
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])


