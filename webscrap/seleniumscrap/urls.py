from django.contrib import admin
from django.urls import path,include
from seleniumscrap import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('selenium',views.login,name='selenium'),
    
]