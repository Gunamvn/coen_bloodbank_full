"""coen_bloodbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Blood Bank
    path('current/', views.currentbbank, name='currentbbank'),
    path('', views.homepage, name='homepage'),
    path('donorreg/', views.donorreg, name='donorreg'),
    path('createreq/', views.createreq, name='createreq'),
    path('changepass/', views.changepass, name='changepass'),
    path('aboutus/', views.aboutus, name='aboutus')
]
