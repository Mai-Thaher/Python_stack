from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.display_result),
    path('lose', views.lose),
    path('again', views.try_again)
]