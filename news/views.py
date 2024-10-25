from django.shortcuts import render
import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from .forms import NewsForm
from .models import News
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
# @login_required
def home_news(request):
    return render(request, "home_news.html")

def show_news(request, id):
    news = News.objects.get(pk = id)
    context = {
        'title' : news.title,
        'author' : news.author,
        'article' : news.article,
        'post_date' : news.post_date,
        'update_date' : news.update_date,
        'pk' : news.pk,
        'news_entries' : News.objects.all()
    }
    return render(request, "news.html", context)

def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        news_entry = form.save(commit=False)
        news_entry.user = request.user
        news_entry.save()
        return HttpResponseRedirect(reverse('news:home_news'))
        # return redirect('news:home_news.html')

    context = {'form': form}
    return render(request, "create_news.html", context)

def edit_news(request, id):
    # Get news entry berdasarkan id
    news = News.objects.get(pk = id)

    # Set news entry sebagai instance dari form
    form = NewsForm(request.POST or None, instance=news)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('news:home_news'))

    context = {'form': form}
    return render(request, "edit_news.html", context)

def delete_news(request, id):
    # Get news berdasarkan id
    news = News.objects.get(pk = id)
    # Hapus news
    news.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('news:home_news'))

def show_xml(request):
    data = News.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = News.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = News.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = News.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")