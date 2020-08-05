from django.contrib import admin

# Register your models here.


from blog.models import Type, Article

# 修改后台admin的标题
admin.site.site_title = '博客管理系统'
admin.site.site_header = '博客管理系统'


# 实体类管理
class ArticleAdmin(admin.ModelAdmin):
    #定制
    list_display = ['title', 'pubtime', 'user']#显示字段
    list_per_page = 10#每页显示的个数
    list_editable = ['pubtime']#列表页可编辑字段
    list_filter = ['pubtime']#过滤条件字段
    search_fields = ['title']#搜索条件字段
    ordering = ['-pubtime']#排序
    date_hierarchy = 'pubtime'

# 注册实体类
admin.site.register(Type)
admin.site.register(Article, ArticleAdmin)
