from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("edit/<int:user_id>/", views.edit_user, name="edit_user"),
    path("account/", views.view_account, name="view_account"),
]
