from django.urls import path
from . import views

urlpatterns=[
path('registerForm',views.index),
path('register',views.RegisterView.as_view()),
path('loginForm',views.login_page),
path('login',views.LoginView.as_view()),
path('home_page',views.home_page),
path('create_playlist',views.create_playlist),
path('add_movies',views.add_movies),
path('get_all_playlist',views.get_all_playlists),
path('get_all_movies_for_playlist/<int:playlistid>/<int:user_id>',views.get_all_movies_for_playlist),
path('get_list_page/<int:playlistid>/<int:user_id>',views.get_list_page)

]