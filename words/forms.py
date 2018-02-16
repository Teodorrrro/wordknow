from django import forms


class WordTranslationForm(forms.Form):
    word_text = forms.CharField(label='Слово:', max_length=100)
    translation_text = forms.CharField(label='Перевод:', max_length=100)
