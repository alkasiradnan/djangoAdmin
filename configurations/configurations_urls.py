from django.urls import path
from configurations import views


urlpatterns = [
    path('/configuration',views.configuration_list,name="configuration_list"),
    path('/configuration/create/', views.configuration_create, name='configuration_create'),
    path('/configuration/(?P<pk>\d+)/update/$', views.configuration_update, name='configuration_update'),
    path('/configuration/(?P<pk>\d+)/delete/$', views.configuration_delete, name='configuration_delete')
]
