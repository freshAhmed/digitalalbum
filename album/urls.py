from django.urls import path

from .views import (create_album ,get_album ,delete_album )


urlpatterns=[
    path('add',create_album),
    path('remove/<str:albumid>',delete_album),
    path('<str:albumid>',get_album),
]