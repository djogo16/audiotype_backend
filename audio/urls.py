from django.urls import path
from . import views


urlpatterns = [
    path('chapter', views.ListAudio.as_view()),
    path('length/', views.RandomAudio.as_view()),
    path('book/', views.SelectedBook.as_view()),
    path('results/', views.ServeResult.as_view()),
    path('books/', views.ListBooks.as_view()),
]



