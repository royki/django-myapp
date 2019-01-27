# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite.books.models import Publisher, Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publishers', 'publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('publication_date',)
	fields = ('title', 'authors' ,'publishers', 'publication_date')
	filter_horizontal = ('authors',)
	raw_id_fields = ('publishers',)
	search_fields = ('first_name', 'last_name')

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'website', 'country')
	search_fields = ('name', 'country')

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)