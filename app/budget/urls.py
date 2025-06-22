from django.urls import path
from . import views

urlpatterns = [
    path('setBudget/', views.set_budget, name='set_budget'),
    path('getAllBudget/', views.get_all_budget, name='get_all_budget'),
    path('editBudger/', views.edit_budget, name='edit_budget'),
    path('deleteBudget/', views.delete_budget, name='delete_budget'),
]
