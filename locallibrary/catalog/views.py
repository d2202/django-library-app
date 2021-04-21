from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """
    Функция отображения домашней страницы сайта
    """
    num_books = Book.objects.all()
    num_instances = BookInstance.objects.all().count()
    num_instances_avaliable = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(request, 'index.html', context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avaliable': num_instances_avaliable,
        'num_authors': num_authors
        })
