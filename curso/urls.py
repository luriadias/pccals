from django.urls import path

from . import views

URLPattern = [

    path("curso/", views.curso),
    path("<slug:slug>/", views.PostDetailView.as_view, name="detail"),
]