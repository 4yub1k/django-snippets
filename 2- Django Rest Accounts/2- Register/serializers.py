class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=75, required=True)
    class Meta:
        model = User
        #fields ="__all__" #change to requred fields
        fields = ['username', 'password', 'email'] #change to requred fields
