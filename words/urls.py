from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user', views.create_user, name='create_user'),
    path('<int:user_id>/words/', views.user_words, name='user_words'),
    path('<int:user_id>/words/new/', views.create_word, name='create_word'),
    path('<int:user_id>/words/<int:word_id>/delete/', views.delete_word, name='delete_word'),
    path('<int:user_id>/words/<int:word_id>/edit/', views.edit_word, name='edit_word'),
]
