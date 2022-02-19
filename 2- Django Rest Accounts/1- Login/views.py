@api_view(['POST'])
def user_login(request):
    if request.method == "POST":

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            data = {}
            username = serializer.data.get("username", None)
            password = serializer.data.get("password", None)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                token = Token.objects.get(user=user)
                data['username']=user.username
                data['email']=user.email
                data['token']=token.key
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"ERROR":"User not found"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
