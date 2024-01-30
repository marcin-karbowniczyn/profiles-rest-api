"""
URL configuration for profiles_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# When a request hits a server, Django will take the URL from the requests, and match it to the first URL it finds here.
# Include is a function we can use to include URLs from other apps in the root project URLs.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
