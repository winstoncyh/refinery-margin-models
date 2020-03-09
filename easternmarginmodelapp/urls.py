"""easternmarginmodelapp URL Configuration

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
from django.urls import path,include
from pages import views

# Add application namespace here using app_name, to differentiate view pages with identical names as in other apps from the view here
namespace = 'emm'
urlpatterns = [
    path('',views.home_view,name='index'),
    path('about/',views.about_view,name='about'),
    path('admin/', admin.site.urls,name='admin'),
    path('margins/<region>/', views.margin_home_view),
    path('margins/', views.margin_home_view,name='margins'),
    path('adminpanel/', admin.site.urls,name='adminpanel'),

]
