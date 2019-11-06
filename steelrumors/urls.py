"""steelrumors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django_registration.backends.activation import urls
from django.urls import path,include
from django.contrib.auth.decorators import login_required as auth
from django.contrib.auth.views import LoginView,logout_then_login
from links.views import LinkListView,UserProfileDetailView,UserProfileEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LinkListView.as_view(), name = 'home'),
    path('login/', LoginView.as_view(template_name="links/login.html"),name='login'),
    path('logout/', logout_then_login,name='logout'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('users/<slug>/',UserProfileDetailView.as_view(),name="profile"),
    path('edit_profile/',auth(UserProfileEditView.as_view()),name="edit_profile"),

]
