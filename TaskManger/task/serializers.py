from rest_framework import serializers
from .models import Category, Task  # Import the Task and Category models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']  # Include the fields you want
        read_only_fields = ['id']  # Make 'id' read-only

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')  # Assuming the Task model has a user field
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'category', 'completed_at', 'user']  # Specify all fields to serialize

    def create(self, validated_data):
        """
        Create and return a new Task instance, given the validated data.
        """
        # Extract category data from validated_data
        category = validated_data.pop('category', None)
        
        # Create the Task instance, setting the category if provided
        task = Task.objects.create(category=category, **validated_data)
        return task

    def update(self, instance, validated_data):
        """
        Update and return an existing Task instance, given the validated data.
        """
        # Check if the status is being updated to "Completed"
        if validated_data.get('status') == Task.COMPLETED and instance.status != Task.COMPLETED:
            instance.mark_complete()

        # Update category if provided
        category = validated_data.pop('category', None)
        if category:
            instance.category = category
        
        # Update the rest of the fields
        return super().update(instance, validated_data)
