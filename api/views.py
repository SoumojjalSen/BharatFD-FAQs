"""Views for the API."""
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer


class FAQListCreateView(generics.ListCreateAPIView):
    """View for listing and creating FAQs."""
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        """
        Add the 'lang' parameter to the serializer context.

        Returns:
            dict: The context dictionary with the 'lang' parameter.
        """
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'en')
        return context
