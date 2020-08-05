"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginViews.as_view()),
    path('register/', views.RegistrViews.as_view()),
    path('index/', views.index.as_view()),
    path('tinymce',include('tinymce.urls')),
    path('blog_add/', views.BlogAddView.as_view()),
    path('updata_blog/', views.BlogUpdataView.as_view()),
    path('delete_blog/', views.BlogDeleteView.as_view()),
    path('blog_detail/',views.BlogDetailView.as_view())
]

