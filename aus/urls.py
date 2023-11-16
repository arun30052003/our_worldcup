from aus.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('pat/',pat,name='pat'),
    path('glenn/',glenn,name='glenn'),
]