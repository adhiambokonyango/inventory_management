"""inventoryManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from officers import views as officer_views
from inventory import views as inventory_views
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('register/', officer_views.register, name='register'),
    path('contact/', contact_views.contact, name='contact'),
    path('contact_upload/', contact_views.contact_upload, name='contact_upload'),
    path('laptops/', inventory_views.laptops, name='laptops'),
    path('desktops/', inventory_views.desktops, name='desktops'),
    path('mobiles/', inventory_views.mobiles, name='mobiles'),

    path('profile/', officer_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='officers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='officers/logout.html'), name='logout'),

]
