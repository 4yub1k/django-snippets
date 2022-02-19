from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from restapi.serializers import UserSerializer

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()
            token=Token.objects.create(user=user)
            data['username']=user.username
            data['email']=user.email
            data['token']=token.key
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
