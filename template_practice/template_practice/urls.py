from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("meal_app.urls")),
    path("admin/", admin.site.urls),
]
