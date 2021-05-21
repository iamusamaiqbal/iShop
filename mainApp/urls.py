from django.conf.urls import re_path
from mainApp import views


urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^contact/', views.contact, name='contact'),
    re_path(r'^about/', views.about, name='about'),

    re_path(r'^product/(?P<id>\d+)/$', views.product_detail, name='product'),
    re_path(r'^addtocart/(?P<id>\d+)/$', views.add_to_cart, name='addtocart'),
    re_path(r'^showcart/(?P<id>\d+)/$', views.show_cart, name='showcart'),
    re_path(r'^showbycat/(?P<id>\d+)/$', views.show_by_cat, name='showbycat'),

    re_path(r'^s$', views.s_register, name='s'),
    re_path(r'^loginUser$', views.login, name='login'),
    re_path(r'^register', views.register, name='register'),
    re_path(r'^logoutUser', views.logout, name='logoutuser'),
]
