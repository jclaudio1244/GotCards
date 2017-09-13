from django.conf.urls import url

from . import views

app_name = 'gameplay'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^catalog$', views.CatalogView.as_view(), name='catalog'),
]