from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField,SerializerMethodField,ValidationError

from django.contrib.auth import get_user_model

User = get_user_model()


######### REGISTER
class UserCreateSerializer(serializers.ModelSerializer):
    email2 = serializers.EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {'password':
        {'write_only':True}
        }
    
    # def validate(self,data):
    #     email = data['email']
    #     user_qs = User.objects.filter(email=email)
    #     if user_qs.exists():
    #         raise ValidationError('Email Already Exists')
    #     return data

    def validate_email(self,value):
        data = self.get_initial()
        email1 = data.get('email2')
        email2 = value
        if email1 != email2:
            raise ValidationError('Email Must Match')

        user_qs = User.objects.filter(email= email2)
        if user_qs.exists():
            raise ValidationError('Email ALready Exists')
        return value

    def validate_email2(self,value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('Email Must Match')
        return value

    def create(self,validate_data):
        username = validate_data['username']
        email = validate_data['email']
        password = validate_data['password']
        user_obj = User(
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validate_data


### LOGIN
class UserLogiSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email  = serializers.EmailField(label='Email')
    token = serializers.CharField(allow_blank=True,read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {'password': {'write_only':True}}