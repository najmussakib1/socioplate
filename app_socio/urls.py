from . import views
from django.urls import path, include


urlpatterns = [
    path('',views.blankpath,name=''),
    path('signin/',views.signin,name='signin'),
    path('search/',views.search,name='search'),
    path('create/',views.create,name='create'),
    path('log-out/',views.handle_logout,name='hand'),
    path('myprof/',views.myprof,name='myprof'),
    path('anotheruser/<str:user>/',views.anotheruser,name='anotheruser'),
    path('createpost/',views.createpost,name='createpost'),
    path('likepost/<int:post_id>/',views.likepost,name='likepost'),
    path('developer/',views.developer,name='developer'),
    
]