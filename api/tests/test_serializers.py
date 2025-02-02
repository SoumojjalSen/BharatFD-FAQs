"""
This file contains the test cases for the serializers.

These tests ensure that the serializers correctly transform the FAQ model instances
into the desired JSON format and handle translations appropriately.
"""

from api.models import FAQ
from api.serializers import FAQSerializer


def test_faq_serializer():
    """
    This file contains the test cases for the serializers.

    These tests ensure that the serializers correctly transform the FAQ model instances
    into the desired JSON format and handle translations appropriately.
    """
    faq = FAQ(question="What is Django?", answer="Django is a web framework.")
    serializer = FAQSerializer(faq, context={"lang": "en"})
    assert serializer.data["question"] == "What is Django?"
    assert serializer.data["answer"] == "Django is a web framework."
