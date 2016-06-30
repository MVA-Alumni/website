from django.conf.urls import patterns, include, url
from django.conf import settings
from directory import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.mylogin, name='login'),
    url(r'^login/(?P<username>.+)/(?P<token>.+)$', views.login_token, name='login_token'),
    url(r'^logout$', views.mylogout, name='logout'),
    url(r'^search_name$', views.search_name, name='search_name'),
    url(r'^search_year$', views.search_year, name='search_year'),
    url(r'^search_domain$', views.search_domain, name='search_domain'),
    url(r'^search_keyword$', views.search_keyword, name='search_keyword'),
    url(r'^me_identity$', views.me_identity, name='me_identity'),
    url(r'^me_contact$', views.me_contact, name='me_contact'),
    url(r'^me_about$', views.me_about, name='me_about'),
    url(r'^add$', views.add, name='add'),
    url(r'^list_users$', views.list_users, name='list_users'),
    url(r'^first_user$', views.first_user, name='first_user'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^alumnus/([\w.]+)$', views.alumnus, name='alumnus'),
    url(r'^year/(\d+)$', views.year, name='year'),
    url(r'^domain/(\d+)$', views.domain, name='domain'),
)
