"""This file contains the form for the FAQ model."""
from django import forms
from api.models import FAQ

class FAQForm(forms.ModelForm):
    """
    Form for the FAQ model.

    This form is used to create and update FAQ instances.

    Attributes:
        Meta (class): Meta class for the FAQForm.
    """
    class Meta:
        """
        Meta class for the FAQForm.

        Attributes:
            model (FAQ): The model associated with this form.
            fields (list): The fields to include in the form.
        """
        model = FAQ
        fields = ['question', 'answer']
