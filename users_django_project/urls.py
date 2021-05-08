"""users_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users import views


urlpatterns = [
    path("", views.UsersListView.as_view(), name="users"),
    path("add_user/", views.AddUser.as_view(), name="add-user"),
    path("get_user/<int:pk>", views.UserDetailView.as_view(), name="get-user"),
    path("edit_user/<int:pk>", views.EditUser.as_view(), name="edit-user"),
    path("delete_user/<int:pk>", views.DeleteUserView.as_view(), name="delete-user"),
    path('admin/', admin.site.urls),
]
