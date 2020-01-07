from django.urls import path
from writer_definition import views

urlpatterns  = [
        path('/writer',views.writer_definition_list,name="writer_definition_list"),
        path('/writer/create/', views.writer_definition_create, name='writer_definition_create'),
        path('/writer/(?P<pk>\d+)/update/$', views.writer_definition_update, name='writer_definition_update'),
        path('/writer/(?P<pk>\d+)/delete/$', views.writer_definition_delete, name='writer_definition_delete')
]
