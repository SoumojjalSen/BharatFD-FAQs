"""Models for the API app."""
import asyncio
from django.db import models
from django.core.cache import cache
from googletrans import Translator
from ckeditor.fields import RichTextField
from .utils.languages import LANGUAGES

class FAQ(models.Model):
    """Model for frequently asked questions."""
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def get_translated_text(self, lang, field):
        """Return the translated text for the given language."""
        cache_key = f'faq_{self.id}_{field}_{lang}'
        translated_text = cache.get(cache_key)
        if not translated_text:
            if lang in LANGUAGES:
                translated_text = getattr(self, f'{field}_{lang}') or getattr(self, field)
            else:
                translated_text = getattr(self, field)
            cache.set(cache_key, translated_text)
        return translated_text

    def save(self, *args, **kwargs):
        translator = Translator()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        for lang in LANGUAGES:
            question_attr = f'question_{lang}'
            answer_attr = f'answer_{lang}'
            if not getattr(self, question_attr):
                setattr(self, question_attr, loop.run_until_complete(
                    translator.translate(self.question, dest=lang)).text)
            if not getattr(self, answer_attr):
                setattr(self, answer_attr, loop.run_until_complete(
                    translator.translate(self.answer, dest=lang)).text)
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the question."""
        return str(self.question)
