from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UsersSerializer
from django.http import JsonResponse


def user_list(request):
    # Get all users from the database
    users = Users.objects.all()
    # Serialize the queryset
    serializer = UsersSerializer(users, many=True)
    # Return a JSON response
    return JsonResponse(serializer.data, safe=False)

class UserCreate(APIView):
    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
