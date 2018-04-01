from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Post(models.Model):
    """
    """
    title = models.CharField(max_length=70)  # 标题
    body = models.TextField()   # 正文
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，blank=True 可以允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    # 一对多, 外键，一个文章只有一个分类， 但一个分类可以用于多个文章
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # 多对多, 一个文章可以有多个标签，一个标签页可以用于多篇文章
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})