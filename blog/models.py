from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    pwd = models.CharField(max_length=32)

    class Meta:
        db_table = 'user'

    # 调整列表页面的显示   中文显示
    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False, verbose_name='类型名称')

    class Meta:
        db_table = 'type'
        verbose_name = '博客文章类型'
        verbose_name_plural = verbose_name

    # 调整列表页面的显示   中文显示
    def __str__(self):
        return self.name


from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name='标题')
    content = HTMLField(verbose_name='内容')
    pubtime = models.DateTimeField(verbose_name='时间')
    pic = models.ImageField(verbose_name='图片', null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='用户')
    type = models.ManyToManyField(to=Type, verbose_name='所属类型')

    class Meta:
        db_table = 'article'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    # 调整列表页面的显示   中文显示
    def __str__(self):
        return self.title
