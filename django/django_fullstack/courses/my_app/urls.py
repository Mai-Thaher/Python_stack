from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_course),
    path('courses/destroy/<int:id>', views.delete_message),
    path('cancel', views.cancel_delete),
    path('destroy/<int:id>', views.delete_course)
]