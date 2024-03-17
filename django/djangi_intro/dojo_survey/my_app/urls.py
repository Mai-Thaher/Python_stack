from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.get_result),
    path('success', views.success),
    path('back', views.go_back)
]