from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('lesson/<str:url>/', lesson, name='lesson'),
]