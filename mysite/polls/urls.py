from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/' , views.detail , name='detail'),
    # result
    path('<int:question_id>/results/' , views.results, name ='results'),
    # vote
    path('<int:question_id>/vote/' , views.vote, name = 'vote'),
    # added the word 'specifics'   
    # delete in namespacing??
    path('specifics/<int:question_id>/', views.detail, name='detail'),

]