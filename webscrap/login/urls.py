from django.contrib import admin
from django.urls import path,include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home_page'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),

]