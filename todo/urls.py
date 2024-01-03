from django.urls import path
from .views import index, task_get, task_post, task_delete, task_update

urlpatterns = [
    path('', index, name='index'),
    path('post', task_post, name='task_post'),
    path('<int:task_id>', task_get, name='task_get'),
    path('delete/<int:task_id>', task_delete, name='task_delete'),
    path('update/<int:task_id>', task_update, name='task_update'),
]