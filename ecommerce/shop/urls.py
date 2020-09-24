from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.index),
    path('about',views.about,name='about'),
    path('contact',views.contact),
    path('productview/<int:myid>',views.productview),
    path('tracker',views.tracker),
    path('search',views.search),
]
