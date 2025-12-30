from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_view, name='loans'),
  path('<int:loan_id>', views.show_views, name='loan'),
  path('new/', views.new_view, name='new_loan'),
  path('new/loans/create/', views.create_view, name='create_loan'),
  path('return/<int:loan_id>', views.return_views, name='return')
]