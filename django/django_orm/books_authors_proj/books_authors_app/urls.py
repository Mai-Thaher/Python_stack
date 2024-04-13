from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('books/<int:id>', views.book_info),
    path('add/<int:id>', views.add_author),
    path('add_book', views.add_book),
    path('authors', views.index_authors),
    path('authors/<int:id>', views.author_info),
    path('add_book/<int:id>', views.add_book_to_list),
    path('add_author', views.add_author_to_table),
]