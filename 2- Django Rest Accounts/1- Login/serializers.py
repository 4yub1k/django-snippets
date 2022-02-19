class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25, required=True)
    password = serializers.CharField(max_length=128, required=True)
