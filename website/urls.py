from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("insights/", views.post_list, name="post_list"),
    path("insights/<slug:slug>/", views.post_detail, name="post_detail"),
]
