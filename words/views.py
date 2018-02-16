from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Word, User
from .forms import WordTranslationForm


def index(request):
    return render(request, 'words/index.html', {
        'users': User.objects.all(),
    })


def create_user(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        User.objects.create(user_name=user_name)
        return redirect(index)
    return render(request, 'words/create_user.html')


def user_words(request, user_id):
    words = Word.objects.filter(user=user_id)
    return render(request, 'words/user_words.html', {
        'user': User.objects.get(pk=user_id),
        'words': words,
    })


def create_word(request, user_id):
    # GET - загрузка страницы; POST - создание word
    form = WordTranslationForm(request.POST or None)
    print(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            word_text = form.cleaned_data['word_text']
            translation_text = form.cleaned_data['translation_text']
            user = User.objects.get(pk=user_id)
            Word.objects.create(user=user, word_text=word_text, translation_text=translation_text)
            return redirect(user_words, user_id)
    return render(request, 'words/create_word.html', {
        'user_id': user_id,
        'form':form,
    })


def delete_word(request, user_id, word_id):
    # GET - загрузка страницы; POST - удаление word
    if request.method == 'POST':
        Word.objects.filter(pk=word_id).delete()
        return redirect(user_words, user_id)
    return render(request, 'words/delete_word.html', {
        'user_id': user_id,
        'word_id': word_id,
    })


def edit_word(request, user_id, word_id):
    # GET - загрузка страницы; POST - удаление word
    word = Word.objects.get(pk=word_id)
    if request.method == 'POST':
        form = WordTranslationForm(request.POST)
        if form.is_valid():
            word_text = form.cleaned_data['word_text']
            translation_text = form.cleaned_data['translation_text']
            user = User.objects.get(pk=user_id)
            Word.objects.filter(user=user, pk=word_id).\
                update(word_text=word_text, translation_text=translation_text)
            return redirect(user_words, user_id)
    else:
        form = WordTranslationForm()
    return render(request, 'words/edit_word.html', {
        # 'user_id': user_id,
        # 'word_id': word_id,
        # 'word': word,
        'form': form,
    })
