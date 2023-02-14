from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('reg', views.RegUser.as_view(), name='reg'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout')
]
