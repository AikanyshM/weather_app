from pydoc import render_doc
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index)
]