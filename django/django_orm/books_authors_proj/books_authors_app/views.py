from django.shortcuts import render, redirect
from . import models
from .models import Author, Book

# This function to display the table of all books found in the database
def index(request):
    context={
        "books": models.display_books()
    }
    return render(request, 'index.html',context)

# This function to add new book from the form (by user) and add it to the previous table
def add_book(request):
    models.add_new_book(request)
    return redirect('/')

# This func display book information after pressing the view link for each book in the table including the list of related authors + display the non-related authors in a dropdown list
def book_info(request,id):
    context={
        "book": models.books_details(id),
        "authors": models.excluded_authors(id),
    }
    return render(request, 'book.html',context)

# This function allow the user to add a new author from thedropdown list to authors list in the book information page
def add_author(request,id):
    book=models.books_details(id)
    author=Author.objects.get(id=request.POST['authors'])
    book=Book.objects.get(id=id)
    book.authors.add(author)
    return redirect(f'/books/{id}')

# the below functions are for the authors

# This function to display the table of all authors found in the database
def index_authors(request):
    context={
        "authors": models.display_all_authors()
    }
    return render(request, 'index_authors.html',context)

# This function to add new author from the form (by user) and add it to the previous table
def add_author_to_table(request):
    return redirect('/authors')

# This func display author information after pressing the view link for each author in the table including the list of related books + display the non-related books in a dropdown list
def author_info(request,id):
    context={
        "author": models.authors_details(id),
        "books": models.excluded_books(id),
    }
    return render(request, 'author.html',context)

# This function allow the user to add a new book from thedropdown list to books list in the author information page
def add_book_to_list(request,id):
    book=Book.objects.get(id=request.POST['books'])
    author=Author.objects.get(id=id)
    author.books.add(book)
    return redirect(f'/authors/{id}')

