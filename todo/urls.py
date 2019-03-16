from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.complete, name='complete'),
    path('deleteComplete', views.deleteCompleted, name='deleteComplete'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
]
