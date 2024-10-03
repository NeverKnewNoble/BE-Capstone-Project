from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.urls')),  # Include task URLs
    path('api/', include('user.urls')),   # Include user URLs
]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/tasks/', include('task.urls')),  # Task-related URLs
#     path('api/users/', include('user.urls')),  # User-related URLs
# ]
