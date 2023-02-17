from django.contrib import admin
from django.urls import path, include
from women.views import WomenAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', WomenAPI.as_view()),
]
