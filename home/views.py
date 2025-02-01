from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from .forms import FAQForm
from .utils.languages import LANGUAGES 

def index(request):
    form = FAQForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    lang = request.GET.get('lang', 'en')
    api_url = request.build_absolute_uri(reverse('faq-list-create')) + f'?lang={lang}'

    try:
        response = requests.get(api_url)
        faqs = response.json() if response.status_code == 200 else []
    except requests.RequestException:
        faqs = []

    context = {
        'form': form,
        'faqs': faqs,
        'lang': lang,
        'languages': LANGUAGES 
    }

    return render(request, 'index.html', context)
