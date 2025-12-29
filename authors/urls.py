from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name= 'authors'),
  path('<int:author_id>', views.show_view, name='author'),
  path('new/', views.new_view, name='new_author'),
  path('new/authors/create/', views.create_view, name='create_author')
]