from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my DRF API!"
    })


@api_view(['POST'])
def logout_route(request):
    logout(request)
    return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)