from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.views import View

from blog.models import User, Type, Article
from blogproject.utils import encryption_md5


class LoginViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        msg = ''
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=name, pwd=encryption_md5(pwd)).count()
        if user:
            req = redirect('/index')
            req.set_cookie('name', name)
            return req
        else:
            msg = "用户名或密码错误"

        return render(request, 'login.html', {'msg': msg})


class RegistrViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registr.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')

        user = User()
        user.name = name
        user.pwd = encryption_md5(pwd)
        user.save()

        return redirect('/login')


class index(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        if name:
            article_list = Article.objects.filter(user__name=name)
            for article in article_list:
                article.type_names = ",".join([i.name for i in article.type.all()])
            cxt = {
                "name": name,
                'article_list': article_list,
            }
            return render(request, 'index.html', cxt)
        else:
            return redirect('/login')

    def post(self, request, *args, **kwargs):
        pass


class BlogAddView(View):
    def get(self, request, *args, **kwargs):
        type_list = Type.objects.all()
        # 准备上下文的数据
        cxt = {
            'type_list': type_list
        }
        # 渲染页面   将cxt字典闯入blog_add页面中
        return render(request, 'blog_add.html', cxt)

    def post(self, request, *args, **kwargs):
        # 获取参数
        title = request.POST.get('title')
        content = request.POST.get('content')
        pic = request.FILES.get("pic")
        type_id = request.POST.getlist('type_id')
        # 当前时间
        pubtime = datetime.datetime.today()
        name = request.COOKIES.get('name')
        user = User.objects.filter(name=name).first()
        Type_id = Type.objects.filter(pk__in=type_id)

        article = Article()
        article.title = title
        article.content = content
        article.pic = pic
        article.pubtime = pubtime
        article.user = user
        article.save()
        for type in Type_id:
            article.type.add(type)
        article.save()
        return render(request, 'index.html', {'name': name})

class BlogDeleteView(View):
    def get(self, request, *args, **kwargs):
        delete_id = request.GET.get('delete_id')
        article = Article.objects.filter(id=delete_id)
        if article:
            article.delete()
            return redirect('/index/')
        return render(request, 'delete_blog.html')


class BlogUpdataView(View):
    def get(self, request, *args, **kwargs):
        type_list = Type.objects.all()
        # 准备上下文的数据
        cxt = {
            'type_list': type_list
        }
        # 渲染页面   将cxt字典闯入blog_add页面中
        return render(request, 'updata_blog.html', cxt)

    def post(self, request, *args, **kwargs):
        updata_id = request.GET.get('updata_id')
        article = Article.objects.get(id=updata_id)
        # 获取参数
        title = request.POST.get('title')
        content = request.POST.get('content')
        pic = request.FILES.get("pic")
        # 当前时间
        pubtime = datetime.datetime.today()
        article.title = title
        article.content = content
        article.pic = pic
        article.pubtime = pubtime
        article.save()
        return render(request,'index.html')
class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        detail_id = request.GET.get('detail_id')
        article = Article.objects.get(id=detail_id)
        cxt = {
            'article':article
        }
        return render(request, 'blog_detail.html',cxt)

