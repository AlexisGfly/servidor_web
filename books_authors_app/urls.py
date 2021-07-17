from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book_views),
    path('show_book', views.show_book_views),
    path('add_author', views.add_author_views),
    path('authors', views.add_an_author_views),
    path('authors_agregado', views.authors_agregado_views),
    path('show_author', views.show_author_views),
    path('add_libro', views.add_libro_views)
]