from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # path('', views.index, name='index'),  for generic view we changed it to belo form:
    path('',views.IndexView.as_view(), name='index'),
   
    # And also dont need the below form for detail  
    # path('<int:question_id>/' , views.detail , name='detail'), 
    # instead:
    path('<int:pk>/', views.DetailView.as_view(), name ='detail'),
    # result
    # path('<int:question_id>/results/' , views.results, name ='results'),
    # changing to:
   path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # vote
    path('<int:question_id>/vote/' , views.vote, name = 'vote'),
]

