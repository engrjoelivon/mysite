from django.conf.urls import include, url,patterns
from blog import views



urlpatterns=patterns('',url(r'^$',views.home,name="home"),
                     url(r'^json/$',views.ret_json,name="ret_json")
                     )