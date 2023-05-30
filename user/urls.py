from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterUserView, CustomTokenObtainPairView, ProfileView, LoginUserView

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    # path('auth/login/', LoginUserView.as_view(), name='login'),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
