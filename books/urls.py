from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name= 'books'),
  path('<int:book_id>', views.show_views, name='book'),
  path('new/', views.new_view, name='new_author'),
  path('new/books/create/', views.create_view, name='create_author')
]