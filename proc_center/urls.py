"""proc_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.i18n import javascript_catalog
import poc_request.views

js_info_dict = {
    'packages': ('django.conf',),
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^thanks/', poc_request.views.thanks),
    url(r'^$', poc_request.views.home),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
    # url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages':'django.conf'}),
] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

