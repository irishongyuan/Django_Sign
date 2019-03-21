from django.urls import path

from . import views

#namespace
app_name = 'acsign'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:activity_id>/', views.detail, name='detail'),
    path('<int:activity_id>/results/', views.results, name='results'),
    path('<int:activity_id>/sign/', views.sign, name='sign'),
]
