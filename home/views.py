"""Views for the home app."""
import requests
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import FAQForm
from .utils.languages import LANGUAGES


def index(request):
    """
    Handle the index view.

    This view handles the display of the FAQ form and the list of FAQs.
    It also handles the form submission for creating new FAQs.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered index page.
    """
    form = FAQForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    lang = request.GET.get('lang', 'en')
    api_url = request.build_absolute_uri(
        reverse('faq-list-create')) + f'?lang={lang}'

    try:
        # Add a timeout of 10 seconds
        response = requests.get(api_url, timeout=10)
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
