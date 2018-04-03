from django import template
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    # dates 方法会返回一个列表，其中为元素为每一篇文章的创建时间，且是Python的date对象，精确到月份，降序排列
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()