from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListCreateView, TaskDetailView, mark_complete, mark_incomplete, CategoryViewSet

# Define a router to automatically generate URLs for ViewSet actions
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),              # GET /tasks/ and POST /tasks/
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),              # GET, PUT, DELETE /tasks/<id>/
    path('tasks/<int:pk>/mark_complete/', mark_complete, name='task-mark-complete'),    # POST /tasks/<id>/mark_complete/
    path('tasks/<int:pk>/mark_incomplete/', mark_incomplete, name='task-mark-incomplete'),  # POST /tasks/<id>/mark_incomplete/
    path('', include(router.urls)),  # Include the router URLs for categories (not nested under 'tasks/')
]
