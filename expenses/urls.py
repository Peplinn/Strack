from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add_expense', views.add_expense, name="add-expenses"),
    path('edit_expense/<int:id>', views.expense_edit, name="expense_edit"),
    path('delete_expense/<int:id>', views.delete_expense, name="delete_expense"),
]
