from django.db import models
from django.urls import reverse
import uuid # понадобится для уникальных экземпляров книг


class Genre(models.Model):
    '''
    Модель, отражающая жанр книги (Science Fiction, non-fiction) и т.п.
    '''
    name = models.CharField(max_length=200, help_text='Enter a book genre.')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100,
        help_text='Enter the language of the book')


    def __str__(self):
        return self.name


class Book(models.Model):
    '''
    Модель, отражающая книгу (в общем смысле)
    '''
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a description of a book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character \
    <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book.')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        '''
        Возвращает url для доступа к конкретному экземпляру книги
        '''
        return reverse('book-detail', args=[str(self.id)])


    def display_genre(self):
        '''
        Возвращает строку из первых трёх жанров (если они существуют)
        нужно для отображения в админке.
        '''
        return ', '.join([genre.name for genre in self.genre.all()[:3] ])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    '''
    Модель для отдельного экзепляра книги
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Uniqie\
        id for this book across the library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.TextField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,
        default='m', help_text='Book avaliability')


    class Meta:
        '''
        Будет использовать данные due_back, чтобы упорядочивать записи
        '''
        ordering = ['due_back']


    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)


class Author(models.Model):
    '''
    Модель, отражающая автора
    '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)


    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
