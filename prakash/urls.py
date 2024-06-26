"""prakash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
    path('', include('django.contrib.auth.urls')),
    path('homepage/',login_required(views.homepage),name="homepage"),
    path("victims/",include("victims.urls")),
    path("volunteers/",include("volunteers.urls")),
    path("home/",include("home.urls")),
    #path('api-auth/', include('rest_framework.urls'))
    #path('victims/', include('victims.urls')),
    path('hospital/',include('hospital.urls')),
    path('timeline/', include('timeline.urls')),
    path('tempstorage/', include('tempstorage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
