from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """
    Функция отображения домашней страницы сайта
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avaliable = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    #для проверки себя, можно передать в шаблон
    num_genres = Genre.objects.count()
    print(num_genres)
    num_books_include_kill = Book.objects.filter(title__icontains="убить").count()
    print(num_books_include_kill)

    return render(request, 'index.html', context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avaliable': num_instances_avaliable,
        'num_authors': num_authors
        })
