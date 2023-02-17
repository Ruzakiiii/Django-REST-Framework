from django.urls import path
from .views import WomenAPI

urlpatterns = [
    path('', WomenAPI.as_view()),
]