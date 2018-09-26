from django.urls import path
from . import views


urlpatterns = [
    path('chapter', views.ListAudio.as_view()),
    path('length/', views.RandomAudio.as_view()),
    path('book/', views.SelectedBook.as_view()),
    path('results/', views.ServeResult.as_view()),
    path('books/', views.ListBooks.as_view()),
    #path('save/', views.SaveScore.as_view()),
    #path('scores/', views.GetScore.as_view()),
    path('auth/register/', views.RegistrationAPI.as_view()),
    path('auth/login/', views.LoginAPI.as_view()),
    path('auth/user/', views.UserAPI.as_view()),

]



