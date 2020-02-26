from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
	path('',views.form_to_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.login,name='login'),
    path('post/',views.post,name='post'),
    path('postpic/',views.postpic,name='post-pic'),
    path('guessed/',views.guessed,name='guessed'),
]
