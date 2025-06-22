from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'disease', 'user', 'created_at')
    search_fields = ('name', 'disease', 'user__email')
    list_filter = ('created_at',)
