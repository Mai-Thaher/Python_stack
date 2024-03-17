from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index ),
    path('add',views.add_on),
    path('show',views.show),
    path('destroy_session', views.destroy)
]