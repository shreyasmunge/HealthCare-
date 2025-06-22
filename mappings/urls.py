from django.urls import path
from .views import MappingViewSet

mapping_list = MappingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

mapping_detail = MappingViewSet.as_view({
    'delete': 'destroy'
})

mappings_for_patient = MappingViewSet.as_view({
    'get': 'doctors_for_patient'
})

urlpatterns = [
    path('', mapping_list, name='mapping-list'),
    path('<int:pk>/', mapping_detail, name='mapping-detail'),
    path('patient/<int:patient_id>/', mappings_for_patient, name='mappings-for-patient'),
]
