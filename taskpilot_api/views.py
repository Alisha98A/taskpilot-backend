from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def logout_route(request):
    response = Response({"message": "Successfully logged out."})
    response.set_cookie(
        key='access',   # hardcoded cookie name
        value='',
        httponly=True,
        max_age=0,
    )
    response.set_cookie(
        key='refresh',  # hardcoded cookie name
        value='',
        httponly=True,
        max_age=0,
    )
    return response