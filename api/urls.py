"""This module contains the URL configuration for the API app."""
from django.urls import path
from .views import FAQListCreateView

urlpatterns = [
    path('faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
]
