from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name= 'books'),
  path('<int:book_id>', views.show_views, name='book')
]