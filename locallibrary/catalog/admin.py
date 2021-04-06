from django.contrib import admin
from .models import Book, Genre, Author, BookInstance, Language


class AuthorBookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorBookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'id')
    list_filter = ('status',)
    fieldsets = (
     ('General info', {
        'fields': ('book', 'imprint', 'id')
     }),
     ('Availablity', {
        'fields': ('status',)
     })
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
