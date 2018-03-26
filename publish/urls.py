"""publish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from order.api import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/org/', org),
    url(r'^api/area/', area),
    url(r'^api/purcate/', purchasecategory),
    url(r'^api/orderdetail/', orderdetail),
    url(r'^api/bonuspoints/', bonuspoints),
    url(r'^api/orguser/', orguser),
    url(r'^api/bidinfo/', biddinginfo),
    url(r'^api/userinfo/', userprofile),
    url(r'^api/footprint/', footprint),
]
