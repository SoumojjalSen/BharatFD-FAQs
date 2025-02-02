"""Serializers for the API."""
from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    """Serializer for the FAQ model."""
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        """Meta class for the FAQSerializer."""
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        """
        Return the translated question.

        Args:
            obj (FAQ): The FAQ instance.

        Returns:
            str: The translated question.
        """
        lang = self.context.get('lang', 'en')
        return obj.get_translated_text(lang, 'question')

    def get_answer(self, obj):
        """
        Return the translated answer.

        Args:
            obj (FAQ): The FAQ instance.

        Returns:
            str: The translated answer.
        """
        lang = self.context.get('lang', 'en')
        return obj.get_translated_text(lang, 'answer')
