from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('',views.index, name = 'index'),

    path('create/', views.create, name='create'),
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
]