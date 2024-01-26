
from django.urls import path
from .views import UserRegistrationView, UserLoginView, user_logout,UserBankAccountUpdateView 
from transactions.views import change_pass
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ), 
    path('profile/change_pass/',change_pass, name='change_pass'),

]