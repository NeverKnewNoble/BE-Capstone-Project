from django.urls import path
from .views import register_user, login_user, logout_user, user_profile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register_user'), 
    path('logout/', logout_user, name='logout_user'),
    path('profile/', user_profile, name='user_profile'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For obtaining tokens
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing tokens
]
