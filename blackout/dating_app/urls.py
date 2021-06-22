"""the_wall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views
# All the paths should get a wall/ since it was included in the_wall's urls.py
urlpatterns = [
    path('', views.dashboard),
    path('edit/<int:user_id>', views.edit_user),
    path('edit/<int:user_id>/update', views.update),
    path('edit/<int:user_id>/addpicture', views.image_upload_view),
    path('submit', views.create_profile),
    path('user/<int:user_id>', views.show_userprofile),
    path('matches/<int:user_id>', views.show_matches),
    path('user/<int:user_id>/like', views.add_like),
    path('user/<int:user_id>/dislike', views.remove_like),
]