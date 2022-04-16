from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
import requests
import re

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import SearchRecord
from .forms import SearchRecordCreateForm
from django.utils.translation import gettext as _


def search_records(request):
    records = SearchRecord.objects.order_by('-created_at')
    if request.method == "POST":
        form = SearchRecordCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.count_of_matches = find_and_count(request.POST["url"],request.POST["keywords"])
            post.created_at = timezone.now()
            post.save()
            return redirect('search_records')
    else:
        form = SearchRecordCreateForm()
        form.fields['url'].label = _('url')
        form.fields['keywords'].label = _('keywords')

    return render(request, 'record/list.html', {'records': records, 'form': form})

def delete_search(request,id):
    a = SearchRecord.objects.get(pk = id)
    a.delete()
    return redirect('search_records')

def find_and_count(url='', keywords=''):
    r = requests.get(url)
    return len(re.findall(keywords, r.content.decode('utf-8')))

def change_language(request, locale='en'):
    from django.utils import translation

    translation.activate(locale)
    return redirect('search_records')