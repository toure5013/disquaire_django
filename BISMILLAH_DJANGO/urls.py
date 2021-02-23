"""BISMILLAH_DJANGO URL Configuration

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
from django.conf import settings
from django.urls import include, path
from django.conf.urls import url

from store import views #import views from store that so we can use the url



urlpatterns = [
    url(r'^$', views.index), #"/store" will call the method "index" in "views.py"
    url(r'^store/', include('store.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
