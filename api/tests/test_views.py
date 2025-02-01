import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from api.models import FAQ


@pytest.mark.django_db
def test_faq_list_create_view():
    client = APIClient()
    url = reverse('faq-list-create')

    # Test creating a new FAQ
    response = client.post(
        url, 
        {'question': 'What is Django?', 'answer': 'Django is a web framework.'}, 
        format='json'
    )
    assert response.status_code == 201
    assert FAQ.objects.count() == 1

    # Test retrieving the list of FAQs
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['question'] == 'What is Django?'
    assert response.data[0]['answer'] == 'Django is a web framework.'
