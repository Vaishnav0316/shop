"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('registerAction/',views.registerAction,name="registerAction"),
    path('loginAction/',views.loginAction,name="loginAction"),
    path('viewuser/',views.viewuser,name="viewuser"),
    path('edit<int:id>/',views.edit,name="edit"),
    path('editAction/',views.editAction,name="editAction"),
    path('delete<int:id>/',views.delete,name="delete"),
    path('uploadfile/',views.uploadfile,name="uploadfile"),
    path('uploadAction/',views.uploadAction,name="uploadAction"),
    path('viewImage/',views.viewImage,name="viewImage"),
    path('viewCountry/',views.viewCountry,name="viewCountry"),
    path('getstate/',views.getstate,name="getstate"),
    path('hidefunction/',views.hidefunction,name="hidefunction"),
    path('mouseevents/',views.mouseevents,name="mouseevents"),
    path('checkuser/',views.checkuser,name="checkuser")

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
