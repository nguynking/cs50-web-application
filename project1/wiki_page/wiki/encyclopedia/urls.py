from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("newPage/", views.newPage, name="newPage"),
    path("edit/<str:entry>", views.edit, name="edit"),
    path("search/", views.search, name="search"),
    path("random/", views.random, name="random"),
]
