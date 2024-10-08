from rest_framework import serializers
from  django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken



class UserSerializer_Deshboard(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields=['id','username','email','name','password',"is_superuser","is_staff"]

    def get_name(self,obj):
        name = obj.first_name
        if name=='':
            name=obj.email
        return name




class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = User
        fields=['id','username','email','name','token']

    def get_token(self,obj):
        token= RefreshToken.for_user(obj)
        return str(token.access_token)

        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['message'] = 'hello world'
        print(self.user.username)
        print('hello')
        return data