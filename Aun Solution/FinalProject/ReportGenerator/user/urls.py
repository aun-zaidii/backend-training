from django.urls import path
from.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name =  'register'),
    path('login/', UserLogin.as_view(), name =  'login'),
    path('logout/', UserLogout.as_view(), name =  'logout'),
    path('user/edit/', UserUpdate.as_view(), name = 'edit_user')


]