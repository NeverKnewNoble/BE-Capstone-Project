from django.urls import path
from .views import register_user, logout_user, user_profile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/register/', register_user, name='register_user'),  # User registration
    path('user/logout/', logout_user, name='logout_user'),        # User logout
    path('user/profile/', user_profile, name='user_profile'),     # Get user profile
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token-based login
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh tokens
]
