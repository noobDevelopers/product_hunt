from django.urls import path
from accounts import views
urlpatterns = [
    
    path('signup/',views.signup,name = 'signup'),
    path('signout/',views.signout,name = 'signout'),
    path('signin/',views.signin,name = 'signin'),
    
]