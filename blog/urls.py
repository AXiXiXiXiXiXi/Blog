from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/new/", views.post_create, name="post_create"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
]
