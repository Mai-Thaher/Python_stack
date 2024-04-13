from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.display_all_shows ),
    path('delete/<int:id>/destroy',views.delete_show ),
    path('shows/<int:id>',views.display_show ),
    path('shows/new',views.add_show_form ),
    path('shows/create',views.add_new_show ),
    path('shows/<int:id>/edit',views.edit_form ),
    path('shows/<int:id>/update', views.update_show)
]