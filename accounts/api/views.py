from .serializers import UserCreateSerializer,UserLogiSerializer

from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,UpdateAPIView

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

###Register
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()



###Login
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLogiSerializer

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = UserLogiSerializer(data= data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data,status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)




