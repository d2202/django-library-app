from django.contrib import admin
from .models import Book, Genre, Author, BookInstance, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
