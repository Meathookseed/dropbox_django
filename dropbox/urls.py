from django.contrib import admin
from dropbox import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('current_user/', views.UserViewSet.as_view({'get': 'retrieve', 'patch': 'update','delete':'destroy'})),
    path('users/', views.UserList.as_view()),
    path('vaults/',views.VaultList.as_view({'get': 'list',
                                            'patch': 'update',
                                            'delete': 'destroy',
                                           'post': 'create'}))
]