"""Admin configuration for the API app."""
from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """Admin class for the FAQ model."""
    list_display = ('question', 'answer')
    search_fields = ('question',)
    list_filter = ('question',)
    fields = ('question', 'answer')
    actions = []

    def has_delete_permission(self, request, obj=None):
        """
        Determine if the delete permission is granted.

        Args:
            request: The current request object.
            obj: The object being deleted.

        Returns:
            bool: True if delete permission is granted, False otherwise.
        """
        return True
