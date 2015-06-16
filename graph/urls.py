from django.conf.urls import patterns, url 
from graph import views 

urlpatterns = patterns('', 
  # The home view ('/graph/') 
  url(r'^$', views.home, name='home'), 
  # Explicit home ('/graph/home/') 
  url(r'^home/$', views.home, name='home'),
  # Redirect to get token ('/graph/gettoken/')
  url(r'^gettoken/$', views.gettoken, name='gettoken'),
  # Me view ('/graph/me/')>
  url(r'^me/$', views.me, name='me'),
  # Mail view ('/graph/mail/')>
  url(r'^mail/$', views.mail, name='mail'),
  # Files view ('/graph/files/')>
  url(r'^files/$', views.files, name='files'),
)
