from django.urls import path
from reader_definition import views


urlpatterns = [
    path('/reader',views.reader_definition_list,name="reader_definition_list"),
    path('/reader/create/', views.reader_definition_create, name='reader_definition_create'),
    path('/reader/(?P<pk>\d+)/update/$', views.reader_definition_update, name='reader_definition_update'),
    path('/reader/(?P<pk>\d+)/delete/$', views.reader_definition_delete, name='reader_definition_delete')
]
