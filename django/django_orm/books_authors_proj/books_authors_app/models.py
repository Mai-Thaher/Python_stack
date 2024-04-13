from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def display_books():
    return Book.objects.all()

def books_details(id):
    return Book.objects.get(id=id)
    
def display_all_authors():
    
    return Author.objects.all()
    
def add_new_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])

def excluded_authors(id):
    book=Book.objects.get(id=id)
    allauthors=book.authors.all()
    return Author.objects.exclude(id__in=allauthors)

def authors_details(id):
    return Author.objects.get(id=id)

def add_new_author(request):
    Author.objects.create(first_name=request.POST['f-name'], last_name=request.POST['l-name'], notes=request.POST['notes'])

def excluded_books(id):
    author=Author.objects.get(id=id)
    allbooks=author.books.all()
    return Book.objects.exclude(id__in=author.books.all())
    # another way >>> return Book.objects.exclude(id__in=allbooks.values_list('id',flat=True))