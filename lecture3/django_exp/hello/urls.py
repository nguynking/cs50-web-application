from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("king", views.king, name="king"),
    path("<str:name>", views.greet, name="greet")
]