from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignupViewSet, CustomTokenObtainPairView, LoginViewSet

# Register SignupViewSet routes
router = DefaultRouter()
router.register(r'users', SignupViewSet, basename='users')

urlpatterns = [
    # User management endpoints
    path('api/', include(router.urls)),

    # JWT Login endpoint
    path('api/login/', LoginViewSet.as_view({'post': 'login'}), name='custom_login'),

    # JWT Token endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
