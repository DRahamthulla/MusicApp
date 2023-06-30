from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

app_name='music'

urlpatterns = [
    path('music_files1/',views.music_files_view, name='music_files1'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.user_logout,name='logout'),
    #path('delete/',views.delete_view,name='delete'),
    #path('music_play/', views.music_player, name='music_play'),
    path('object-details/', views.music_player, name='object-details'),
    #path('upload/<str:value>/', views.upload_view, name='upload'),
    path('homeupload/<str:value>/', views.upload_view, name='upload'),
   path('',views.home_view,name='back'),
   path('music/search/',views.music_search_view,name='sreach'),
]
    # Add other URL patterns if needed
