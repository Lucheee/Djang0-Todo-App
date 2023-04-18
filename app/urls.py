from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update/<int:pk>/', views.update, name='update'),
    path('todo_lists/<int:pk>/', views.todo_lists, name='todo_lists'),
    path('delete/<int:pk>/', views.delete, name='delete' ),
    path('completed/<int:pk>/', views.completed, name='completed' ),
    path('incomplete/<int:pk>/', views.incomplete, name='incomplete' ),
]