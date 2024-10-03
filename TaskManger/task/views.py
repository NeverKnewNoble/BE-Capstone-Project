from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from django.contrib.auth.models import User

# List all tasks with optional filters, and create a new task
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only the authenticated user’s tasks are retrieved
        queryset = Task.objects.filter(user=self.request.user)
        # Filter using query parameters for any valid Task field
        filters = {key: value for key, value in self.request.query_params.items() if key in ['status', 'priority', 'due_date']}
        return queryset.filter(**filters)

    def perform_create(self, serializer):
        # Ensure the task is associated with the authenticated user
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete a specific task by ID
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure only tasks belonging to the authenticated user are retrieved
        return Task.objects.filter(user=self.request.user)

# Mark a task as complete
@api_view(['POST'])
def mark_complete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)  # Ensure user ownership
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if task.status != Task.COMPLETED:  # Prevent re-completing tasks
        task.mark_complete()
        return Response({'message': 'Task marked as complete'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Task is already complete'}, status=status.HTTP_400_BAD_REQUEST)

# Mark a task as incomplete
@api_view(['POST'])
def mark_incomplete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)  # Ensure user ownership
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if task.status == Task.COMPLETED:  # Only mark as incomplete if previously complete
        task.status = Task.PENDING
        task.completed_at = None  # Reset the completed timestamp
        task.save()
        return Response({'message': 'Task marked as incomplete'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Task is not complete'}, status=status.HTTP_400_BAD_REQUEST)

# ************Category view*****************
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
