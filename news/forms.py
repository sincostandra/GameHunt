from django.forms import ModelForm
from .models import News
from django.utils.html import strip_tags

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "article", "author", 
                  ]

    def clean_news_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_article(self):
        article = self.cleaned_data["article"]
        return strip_tags(article)
    
    def clean_author(self):
        author = self.cleaned_data["author"]
        return strip_tags(author)