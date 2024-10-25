from django.forms import ModelForm
from django import forms
from .models import News
from django.utils.html import strip_tags

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "article", "author", 
                  ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter news headline'
                }),
            'article': forms.Textarea(attrs={
                'class': 'form-input', 
                'placeholder': 'Write your article here...'
                }),
            'author': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter news author'
                }),
            }

    def clean_news_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_article(self):
        article = self.cleaned_data["article"]
        return strip_tags(article)
    
    def clean_author(self):
        author = self.cleaned_data["author"]
        return strip_tags(author)