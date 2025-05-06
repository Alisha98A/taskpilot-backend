from django.contrib import admin
from django.urls import path, include
from .views import root_route
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Root route
    path('', root_route),
    
    # Admin route
    path('admin/', admin.site.urls),
    
    # DRF Authentication (Login/Logout)
    path('api-auth/', include('rest_framework.urls')),  # For browsing the API
    
    # DJ Rest Auth - Login/Logout and Password Reset
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # Login/Logout
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration
    
    # JWT Token Obtain and Refresh views
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include tasks app routes
    path('api/', include('tasks.urls')),
]