from django.conf.urls import include, url,patterns
from blog import views


urlpatterns=patterns('',url(r'^$',views.home,name="home"),)