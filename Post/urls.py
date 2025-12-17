from .views import (get_post,add_post,delete_post,home_view,modify_post)
from django.urls import path 
urlpatterns=[
 path('add',add_post),

 path('remove/<str:id>',delete_post),
 path('edit/<str:id>',modify_post),
 path('<str:albumid>/<str:postid>',get_post),

]