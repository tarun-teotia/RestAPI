from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'apiOverview'),
    path('v1/tasks/', views.list_allTasks, name = 'all'),
    path('v1/tasks/add/', views.add_task, name = 'add'),

    path('v1/tasks/addbulk/', views.addBulk_tasks, name = 'addBulk'),

    path('v1/tasks/<int:pk>/', views.specific_task, name = 'Specific'),
    path('v1/tasks/update/<int:pk>/', views.update_task, name = 'update'),
    path('v1/tasks/delete/<int:pk>/', views.delete_task, name = 'del'),

    path('v1/tasks/delete_bulk/', views.delete_bulkTask, name = 'delBulk'),
]