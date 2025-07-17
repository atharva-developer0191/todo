# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # Add Task
    path('addTask/', views.addTask, name='addTask'),
    # Mark Task as Done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark Task as Undone
    path('mark_as-undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    # Edit Task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # # Delete Task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
