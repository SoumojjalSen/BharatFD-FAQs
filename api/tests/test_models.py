import pytest
from api.models import FAQ


@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(
        question="What is Django?", 
        answer="Django is a web framework."
    )
    assert faq.get_translated_text('en', 'question') == "What is Django?"
    assert faq.get_translated_text('en', 'answer') == "Django is a web framework."
