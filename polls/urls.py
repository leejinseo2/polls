from django.urls import path
from . import views

#from config.urls import urlpatterns
from . import views
from .views import results, detail
app_name = 'polls'
urlpatterns =[
    path('',views.index,name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]