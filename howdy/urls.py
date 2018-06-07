from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^$', views.chart,  name='demo'),
    url(r'^catalogue/$', views.CataloguePageView.as_view()),
]


