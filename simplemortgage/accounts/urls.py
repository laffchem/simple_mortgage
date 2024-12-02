from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    path("edit/<int:user_id>/", views.edit_user, name="edit_user"),
    path("account/<int:user_id>", views.view_account, name="profile"),
    path("upload/", views.upload_file, name="upload_file"),
    path("view_pdf/<int:file_id>/", views.view_pdf, name="view_pdf"),
]
