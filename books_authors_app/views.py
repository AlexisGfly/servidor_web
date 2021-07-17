from django.shortcuts import render, redirect 
from django.utils.crypto import get_random_string
import random
from time import gmtime, strftime, localtime

from books_authors_app.models import * 

def index(request):
    context = {"books": Books.objects.all()}		# sólo se envía todos los libros
    return render(request,"index.html",context)

def add_book_views(request): 
    print('\n\n*******add_book_views***********\n\n')
    title_html = request.POST.get("titulo_html")
    descr_html = request.POST.get("description_html")
    # print(title_html)
    # print(descr_html)
    Books.objects.create(title=title_html, desc=descr_html)
    return redirect('/')

def show_book_views(request):
    print('\n\n*********show_book_views*********\n\n')
    book_id = request.POST.get("book_id")
    context = {"books": Books.objects.get(id=book_id),"authors": Books.objects.get(id=book_id).authors.all(),"authors_complete": Authors.objects.all()}
    return render(request,"books.html",context)

def add_author_views(request):
    print('\n\n*********add_author_views*********\n\n')
    autor = request.POST.get("select")
    libro = request.POST.get("libro")
    print(autor)
    print(libro)
    autor__add = Authors.objects.get(id=autor) 
    libro_add = Books.objects.get(id=libro)
    
    autor__add.books.add(libro_add)

    return redirect('/')

def add_an_author_views(request):
    print('\n\n*********add_an_author_views*********\n\n')
    context = {"authors": Authors.objects.all()}		# sólo se envía todos los libros
    return render(request,"author.html",context)

def authors_agregado_views(request): 
    print('\n\n*******authors_agregado_views***********\n\n')
    nombre_html = request.POST.get("nombre_html")
    apellido_html = request.POST.get("apellido_html")
    notas_html = request.POST.get("notas_html")
    print(nombre_html)
    print(apellido_html)

    Authors.objects.create(first_name=nombre_html, last_name=apellido_html, notas = notas_html)
    return redirect('/authors')

def show_author_views(request):
    print('\n\n*********show_author_views*********\n\n')
    author_id = request.POST.get("author_id")
    # context = {"authors": Authors.objects.get(id=author_id),"books": Books.objects.get(id=author_id).books.all(),"books_complete": Books.objects.all()}
    context = {"authors": Authors.objects.get(id=author_id),"books": Authors.objects.get(id=author_id).books.all(),"books_complete": Books.objects.all()}
    return render(request,"author_show.html",context)

def add_libro_views(request):
    print('\n\n*********add_author_2_views*********\n\n')
    autor = request.POST.get("select")
    libro = request.POST.get("libro")
    print(autor)
    print(libro)
    autor__add = Authors.objects.get(id=autor) 
    libro_add = Books.objects.get(id=libro)
    
    libro_add.authors.add(autor__add)

    return redirect('/authors')