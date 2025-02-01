from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)
    list_filter = ('question',)
    fields = ('question', 'answer')
    actions = []

    def has_delete_permission(self, request, obj=None):
        return True
