from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('buy', views.buy, name='buy'),
    path('userinfo.html',TemplateView.as_view(template_name='userinfo.html')),
    path('order.html',TemplateView.as_view(template_name='order.html'))
]
