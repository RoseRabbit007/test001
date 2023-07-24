from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('data_post/',StudentView.as_view(), name='data_post'),
    path('data_get/<int:id>',StudentView.as_view(), name='data_get'),
    path('data_update/<int:id>',StudentView.as_view(), name='data_update'),
    path('data_delete/<int:id>',StudentView.as_view(), name='data_delete'),

    
]