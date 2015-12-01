"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
from django.views.generic import TemplateView
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r"^askquestion/$", forum),
    url(r'^home/$', General.as_view(), name='General'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Homepage/', Homepage),
    url(r'^General/', General.as_view(), name='General'),
    url(r'^wp/', wp.as_view(), name='wp'),
    url(r'^java/', java.as_view(), name='java'),
    url(r'^dbms/', dbms.as_view(), name='dbms'),
    url(r'^Profilepage/', Profilepage),
    url(r'^submit/', post_new),
    url(r'^rome/', IndexView.as_view(), name='index'),
    url(r'^jome/$', post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', post_new, name='post_new'),
)