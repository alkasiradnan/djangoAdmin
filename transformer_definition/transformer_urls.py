from django.urls import path
from transformer_definition import views


urlpatterns = [
    path('/transformer',views.transformer_definition_list,name="transformer_definition_list"),
    path('/transformer/create/', views.transformer_definition_create, name='transformer_definition_create'),
    path('/transformer/(?P<pk>\d+)/update/$', views.transformer_definition_update, name='transformer_definition_update'),
    path('/transformer/(?P<pk>\d+)/delete/$', views.transformer_definition_delete, name='transformer_definition_delete')
]
