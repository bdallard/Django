from django.conf.urls import url
from howdy import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
]



