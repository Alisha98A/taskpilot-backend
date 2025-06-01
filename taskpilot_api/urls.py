from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
from .views import logout_route

urlpatterns = [
    # React front end served at root
    path('', TemplateView.as_view(template_name='index.html')),

    # Admin panel
    path('admin/', admin.site.urls),

    # API
    path('api/api-auth/', include('rest_framework.urls')),
    path(
        'api/dj-rest-auth/logout/',
        logout_route,
        name='logout',
    ),
    path(
        'api/dj-rest-auth/',
        include('dj_rest_auth.urls'),
    ),
    path(
        'api/dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls'),
    ),
    path(
        'api/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh',
    ),

    # Include tasks app routes
    path('api/', include('tasks.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
