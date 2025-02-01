from api.models import FAQ
from api.serializers import FAQSerializer


def test_faq_serializer():
    faq = FAQ(question="What is Django?", answer="Django is a web framework.")
    serializer = FAQSerializer(faq, context={'lang': 'en'})
    assert serializer.data['question'] == "What is Django?"
    assert serializer.data['answer'] == "Django is a web framework."
