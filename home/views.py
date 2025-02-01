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

    api_url = reverse('faq-list-create')
    response = requests.get(request.build_absolute_uri(api_url))
    print('Response', response)
    faqs = response.json()
    if response.status_code == 200:
        faqs = faqs
    else:
        faqs = []
            

    context = {
        'form': form,
        'faqs': faqs,
    }
    return render(request, 'index.html', context)

