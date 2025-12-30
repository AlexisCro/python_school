from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name='categories'),
  path('<int:category_id>', views.show_views, name='category'),
  path('new/', views.new_view, name='new_category'),
  path('new/category/create/', views.create_view, name='create_category')
]