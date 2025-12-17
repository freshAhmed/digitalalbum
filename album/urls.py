from django.urls import path,include

from .views import (create_album ,get_album ,delete_album,edit_album,get_albums )


urlpatterns=[
    path('add',create_album),
    path('remove/<str:albumid>',delete_album),
    path('<str:albumid>',get_album),
    path('edit/<str:albumid>',edit_album),
    path('',get_albums),
    path('posts/',include('Post.urls'))

]