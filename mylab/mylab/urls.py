from django.contrib import admin
from django.urls import path
from dating.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first_page),
    path('check/<int:id_user>',last_page),
    path('check',chec_profil)
]
