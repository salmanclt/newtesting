from django.urls import path
from . import views

urlpatterns = [
    path('fbpage/',views.fn_index),
    path('assign3/',views.fn_index1)
]