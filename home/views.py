from django.shortcuts import render, redirect
from .forms import FAQForm
import requests
from django.urls import reverse

def index(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FAQForm()
    
    lang = request.GET.get('lang', 'en')
    

    api_url = reverse('faq-list-create') + f'?lang={lang}'
    response = requests.get(request.build_absolute_uri(api_url))

    if response.status_code == 200:
        faqs = response.json()
    else:
        faqs = []
            
    context = {
        'form': form,
        'faqs': faqs,
        'lang': lang
    }
    return render(request, 'index.html', context)

