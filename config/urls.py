from django.contrib import admin
from django.urls import path

from django.urls import path

from main.views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TagListCreateView, \
    TagRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', TaskListCreateView.as_view(), name='task-list-create'),
    path('hello/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('how/', TagListCreateView.as_view(), name='tag-list-create'),
    path('ho/<int:pk>/', TagRetrieveUpdateDestroyView.as_view(), name='tag-retrieve-update-destroy'),
]
